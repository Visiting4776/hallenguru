<script>
	import Event from "./components/Event.svelte";
	import EventsList from "./components/EventsList.svelte";
	
    async function fetchTickets() {
        const res = await fetch("./get_bath_info");
        const json= await res.json();
        
        // update date string that was given from JSON
        return json.map(e => 
            ({...e, date: new Date(e.date).setHours(0,0,0,0)})
        );
    }
    function refreshPage() {
        events_promise = fetchTickets();
    }

    let today = new Date().setHours(0,0,0,0);
    let events_promise = fetchTickets();
</script>

<div class="mt-2 mx-auto max-w-xl bg-white shadow-md px-3 py-5">
<button on:click={refreshPage}>Refresh</button>


{#await events_promise}
	<p>...waiting</p>
{:then events}
    <EventsList name="Today" events={events} filter={e => e.date === today}/>
    <EventsList name="Later Dates" events={events} filter={e => e.date > today}/>
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}
</div>

<style global lang="postcss">
	@tailwind base;
	/* @tailwind components; */
	@tailwind utilities;
</style>