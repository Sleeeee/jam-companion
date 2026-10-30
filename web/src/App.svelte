<script lang="ts">
  import { ModeWatcher } from "mode-watcher";
  import { Header, Player } from "$lib/components/custom";

  let result = 'Loading...';

  fetch('/api/')
    .then((response) => response.json())
    .then((data) => {
      result = data.message;
    })
    .catch((error) => {
      result = `Error: ${error.message}`;
    });
</script>

<ModeWatcher />

<main class="min-h-screen w-9/10 mx-auto bg-gray-200 text-gray-800 dark:bg-gray-800 dark:text-gray-200">
  <Header />
  <Player />
</main>
