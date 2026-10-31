<script lang="ts">
  import { onMount, setContext } from "svelte";
  import { AlphaTabApi, LayoutMode, ScrollMode } from "@coderline/alphatab";
  import type { json, RenderingResources } from "@coderline/alphatab";
  import { mode } from "mode-watcher";
  import { Controls, Score } from "./player";

  let element: HTMLDivElement | null = $state(null);
  let scrollElement: HTMLDivElement | null = $state(null);

  let alphaTabContext: AlphaTabApi | null = $state({ api: null });
  setContext("alphatab", alphaTabContext);

  const colorsLight: RenderingResources = {
    barNumberColor: "#1e2939", // gray-800
    barSeparatorColor: "#1e2939",
    mainGlyphColor: "#1e2939",
    scoreInfoColor: "#1e2939",
  };
  const colorsDark: RenderingResources = {
    barNumberColor: "#e5e7eb", // gray-200
    barSeparatorColor: "#e5e7eb",
    mainGlyphColor: "#e5e7eb",
    scoreInfoColor: "#e5e7eb",
  };

  onMount(() => {
    const api: AlphaTabApi = new AlphaTabApi(element, {
      core: {
        file: "/static/in_flames-only_for_the_weak.gp",
        fontDirectory: "/font/",
      },
      display: {
        layoutMode: LayoutMode.Horizontal,
        resources: mode.current === "light" ? colorsLight : colorsDark,
      },
      player: {
        enablePlayer: true,
        enableCursor: true,
        enableAnimatedBeatCursor: true,
        enableElementHighlighting: true,
        nativeBrowserSmoothScroll: true,
        scrollMode: ScrollMode.Smooth,
        scrollOffsetX: -250,
        scrollElement,
        soundFont: "/soundfont/sonivox.sf2",
      },
    } satisfies json.SettingsJson);

    api.renderFinished.on(() => {
      console.log("Rendering finished");
    });

    alphaTabContext.api = api;

    return () => {
      alphaTabContext.api = null;
      api.destroy();
    };
  });

  $effect(() => {
    if (!alphaTabContext.api) return;

    alphaTabContext.api.settings.fillFromJson({
      display: {
        resources: mode.current === "light" ? colorsLight : colorsDark,
      },
    });

    alphaTabContext.api.updateSettings();
    alphaTabContext.api.render();
  });
</script>

<Score bind:element bind:scrollElement />
<Controls />
