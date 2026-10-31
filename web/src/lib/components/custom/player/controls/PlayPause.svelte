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

  const handleKeyDown = (event) => {
    if (event.code === "Space") {
      togglePlay();
    }
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

<svelte:window on:keydown|preventDefault={handleKeyDown} />

<Button onclick={togglePlay} class="my-auto">
  {#if isPlaying}
    <PauseIcon />
  {:else}
    <PlayIcon />
  {/if}
</Button>
