<script lang="ts">
  import { Tile, Content } from "carbon-components-svelte";
  import SvelteMarkdown from "svelte-markdown";
  import CircleDash from "carbon-icons-svelte/lib/CircleDash.svelte";

  import { DoctorSocket, type TranscriptMessage } from "../types";
  import { onMount } from "svelte";

  let live: string;
  let loading = false;

  // Function to filter out non-English text
  function filterEnglishText(text: string): string {
    // This is a simple filter that removes lines with non-ASCII characters
    // You might want to use a more sophisticated method for better accuracy
    return text.split('\n')
      .filter(line => /^[\x00-\x7F]*$/.test(line))
      .join('\n');
  }

  onMount(async () => {
    DoctorSocket.on("transcript", (x) => {
      console.log(x);
      loading = true;
      // Apply the filter before setting the live variable
      live = filterEnglishText(x).replaceAll("\n", "\n\n");
    });
  });
</script>

<div
  class="h-full border-2 border-gray-600 border-solid flex flex-col overflow-x-hidden"
>
  <Tile class="w-full flex justify-between">
    <p class="text-lg">Your conversation</p>
    <CircleDash
      class="w-6 h-6 block  {loading && 'animate-duration-[1s] animate-pulse'}"
    />
  </Tile>

  <Content class="overflow-y-scroll">
    {#if live}
      <SvelteMarkdown source={live} />
    {:else}
      <p class="text-gray-500">Conversation transcripts go here</p>
    {/if}
  </Content>
</div>