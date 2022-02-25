<script>
    import Event from "./Event.svelte";
    export let name;
    export let events;
    export let filter;
</script>

<h1 class="text-4xl">{name}</h1>
<div class="space-y-3 divide-y divide-solid">
	{#each events.filter(filter) as event}
		<Event {event}/>
    {:else}
        no events matching criteria!
	{/each}
</div>