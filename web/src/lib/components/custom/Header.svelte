<script lang="ts">
  import { toggleMode } from "mode-watcher";
  import { Button, Input } from "$lib/components/ui";
  import MoonIcon from "@lucide/svelte/icons/moon";
  import SearchIcon from "@lucide/svelte/icons/search";
  import SunIcon from "@lucide/svelte/icons/sun";
</script>

<header
  class="border-b border-gray-300 bg-gray-200 px-4 py-3 text-gray-900 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-100"
>
  <div class="mx-auto flex max-w-screen-2xl items-center gap-4">
    <div class="flex shrink-0 items-center gap-2">
      <img src="/favicon.svg" alt="Jam Companion" class="size-8" />
      <h1 class="text-lg font-semibold">Jam Companion</h1>
    </div>

    <div class="flex flex-1 justify-center">
      <div class="relative w-full max-w-md">
        <SearchIcon size={18} class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500" />
        <Input
          placeholder="Search..."
          class="h-9 border-gray-300 bg-gray-100 pl-9 dark:border-gray-600 dark:bg-gray-700"
        />
      </div>
    </div>

    <Button
      onclick={toggleMode}
      variant="outline"
      size="icon"
      aria-label="Toggle dark mode"
      class="size-9 border-gray-300 bg-gray-100 dark:border-gray-600 dark:bg-gray-700"
    >
      <SunIcon class="dark:hidden" />
      <MoonIcon class="hidden dark:block" />
    </Button>
  </div>
</header>
