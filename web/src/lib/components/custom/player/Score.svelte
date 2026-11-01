<script lang="ts">
  import { ScrollArea } from "$lib/components/ui";

  let { element = $bindable(null), scrollElement = $bindable(null) } = $props();

  const handleWheel = (event: WheelEvent) => {
    if (!scrollElement) {
      return;
    }

    event.preventDefault();
    scrollElement.scrollLeft += event.deltaY;
  };

  $effect(() => {
    if (!scrollElement) {
      return;
    }

    scrollElement.addEventListener("wheel", handleWheel);
    return () => {
      scrollElement.removeEventListener("wheel", handleWheel);
    };
  });
</script>

<ScrollArea bind:viewportRef={scrollElement} orientation="horizontal" class="p-4">
  <div bind:this={element}></div>
</ScrollArea>
