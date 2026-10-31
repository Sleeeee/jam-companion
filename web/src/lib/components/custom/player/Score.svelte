<script lang="ts">
  import { ScrollArea } from "$lib/components/ui";

  let { element = $bindable(), scrollElement = $bindable() }: ScoreProps = $props();
</script>

<ScrollArea bind:viewportRef={scrollElement} orientation="horizontal" class="p-4">
  <div bind:this={element} />
</ScrollArea>
