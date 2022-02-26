<script>
    import Event from "./Event.svelte";
    export let name;
    export let events;
</script>
<div>
<h1 class="text-3xl pb-1 font-serif border-b-2 border-gray-600 text-gray-600">{name}</h1>
<div class="space-y-3 divide-y divide-solid">
	{#each events as event}
		<Event {event}/>
    {:else}
        <p>No events matching this filter.</p>
	{/each}
</div>
</div>