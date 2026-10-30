<script lang="ts">
  import { getContext } from "svelte";
  import { Button } from "$lib/components/ui";
  import { AlphaTabApi, synth } from "@coderline/alphatab";
  import PauseIcon from "@lucide/svelte/icons/pause";
  import PlayIcon from "@lucide/svelte/icons/play";

  const alphaTabContext = getContext("alphatab");
  let isPlaying: boolean = $state(false);

  const togglePlay = () => {
    alphaTabContext.api?.playPause();
  };

  $effect(() => {
    const api = alphaTabContext.api;
    if (!api) return;

    const playerStateChangedHandler = (event) => {
      isPlaying = event.state === synth.PlayerState.Playing;
    };

    api.playerStateChanged.on(playerStateChangedHandler);
    return () => {
      api.playerStateChanged.off(playerStateChangedHandler);
    };
  });
</script>

<Button onclick={togglePlay}>
  {#if isPlaying}
    <PauseIcon />
  {:else}
    <PlayIcon />
  {/if}
</Button>
