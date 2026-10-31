<script lang="ts">
  import { getContext } from "svelte";
  import * as Popover from "$lib/components/ui/popover/index.ts";
  import { buttonVariants } from "$lib/components/ui/button/index.ts";
  import type { Track } from "@coderline/alphatab";
  import ListIcon from "@lucide/svelte/icons/list";

  const alphaTabContext = getContext("alphatab");
  let tracks: Track[] = $state([]);

  $effect(() => {
    const api = alphaTabContext.api;
    if (!api) return;

    const scoreLoadedHandler = (score) => {
      tracks = score.tracks;
    };

    api.scoreLoaded.on(scoreLoadedHandler);
    return () => {
      api.scoreLoaded.off(scoreLoadedHandler);
    };
  });
</script>

<Popover.Root>
  <Popover.Trigger class={buttonVariants({ variant: "outline", class: "w-fit" })}>
    <ListIcon />
    Tracks
  </Popover.Trigger>

  <Popover.Content>
    {#each tracks as track}
      <p>
        {track.name}
      </p>
    {/each}
  </Popover.Content>
</Popover.Root>
