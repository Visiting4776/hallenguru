<script>
	import Event from "./components/Event.svelte";
	import EventsList from "./components/EventsList.svelte";
	
    async function fetchTickets() {
        const res = await fetch("./api/baths");
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
    let show_reserved = true;
    $: allowed_states = show_reserved ? ['available', 'reserved'] : ['available'];
    let events_promise = fetchTickets();
</script>

<div class="mt-2 mx-auto max-w-xl bg-white text-gray-700 shadow-md pt-2 pb-5 backdrop-blur-md">
    <div class="py-3 px-3 flex flex-row items-center justify-between sticky top-0 bg-white/60 bg-blur">
        <h1 class="text-4xl font-serif flex flex-row items-center justify-between">Hallenguru <div class="ml-3 swimmer">🏊</div></h1>
        <button class="px-1" on:click={refreshPage}>Refresh Page</button>
    </div>
    <div class="mt-3 px-6">
        <label class="mb-3">
            <input type=checkbox bind:checked={show_reserved}>
            Show reserved slots (these might become available again later)
        </label>

        <div class="space-y-8">
        {#await events_promise}
            <p>Loading</p>
        {:then events}
            
            <EventsList name="Today" events={
                events.filter(e => e.date === today && allowed_states.includes(e.state))
                .sort((a,b) => {a.start_time < b.start_time})
            }/>
            <EventsList name="Later Dates" events={events.filter(e => e.date > today && allowed_states.includes(e.state))}/>
            
        {:catch error}
            <p style="color: red">{error.message}</p>
        {/await}
        </div>
    </div>
</div>

<style global lang="postcss">
    @font-face {
		font-family: EB Garamond;
		src: url(/fonts/EBGaramond-SemiBold.ttf);
	}

	@tailwind base;
	@tailwind components;
	@tailwind utilities;

    .bg-blur{
        backdrop-filter: blur(5px);
    }
    .swimmer{
        transform: scale(-1.5, 1.6);
    }
</style>