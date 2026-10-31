<script lang="ts">
  import { PlayPause, TrackSelector } from "./controls";
</script>

<footer class="fixed bottom-0 inset-x-0 z-10 h-1/20">
  <div class="mx-auto flex items-center justify-center gap-4 px-6">
    <TrackSelector />
    <PlayPause />
  </div>
</footer>
