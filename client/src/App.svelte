<script>
	import Event from "./components/Event.svelte";
	
    async function fetchTickets() {
        const res = await fetch("./get_bath_info");
	    return res.json();
    }
    function refreshPage() {
        events_promise = fetchTickets();
    }

    let events = [];
    let events_promise = fetchTickets();
</script>

<div class="mt-2 mx-auto max-w-xl bg-white shadow-md px-3 py-5">
<button on:click={refreshPage}>Refresh</button>
<h1>Today</h1>
{#await events_promise}
	<p>...waiting</p>
{:then events}
<div class="space-y-3 divide-y divide-solid">
	{#each events as event (event.id)}
		<Event {event}/>
	{/each}
</div>
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}
</div>

<style global lang="postcss">
	@tailwind base;
	/* @tailwind components; */
	@tailwind utilities;
</style>