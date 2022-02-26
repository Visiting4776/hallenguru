<script>
	import EventsList from "./components/EventsList.svelte";
	
    async function fetchTickets() { //returns a promise
        //TODO: instead make API call and get bath info from server
        let all_events = [];
        parsed_baths = 0;

        await Promise.all(bath_ids.map(async (id) => {
            const res = await fetch(`./api/ticketinfo/${id}`);
            const json= await res.json(); //a list of objects, not a string

            all_events = [...all_events, ...json];
            parsed_baths++;
        }))

        // update date string that was given from JSON
        return all_events.map(e => 
            ({...e, date: new Date(e.date).setHours(0,0,0,0)})
        );
    }

    function refreshPage() {
        events_promise = fetchTickets();
    }

    function eventSorter(a, b) {
        if(a.start_time < b.start_time) {return -1};
        if(a.start_time > b.start_time) {return 1};
        return 0;
    }

    const bath_ids = [1,2,7,9,11,15,17,18,19,21,24,26,27,28,29,30,31,34,38,42,43,45,46,47,48,49,51,52,54,60,61,62,64,68,70,71,74,76,79,81];
    let parsed_baths = 0;
    let today = new Date().setHours(0,0,0,0);

    let show_reserved = true;
    $: allowed_states = show_reserved ? ['available', 'reserved'] : ['available'];

    let events_promise = fetchTickets();
</script>

<div class="mt-2 mx-auto max-w-xl bg-white text-gray-700 shadow-md pt-2 pb-5 backdrop-blur-md">
    <div class="py-3 px-3 flex flex-row items-center justify-between sticky top-0 bg-white/60 bg-blur">
        <h1 class="text-4xl font-serif flex flex-row items-center justify-between">Hallenguru <div class="ml-3 swimmer">🏊</div></h1>
        <button class="px-1" on:click={refreshPage} disabled={parsed_baths<bath_ids.length}>Refresh Page</button>
    </div>
    <div class="mt-3 px-6">
        <label class="mb-3">
            <input type=checkbox bind:checked={show_reserved}>
            Show reserved slots (these might become available again soon)
        </label>

        <div class="space-y-8">
        {#await events_promise}
            <p>Loading: {parsed_baths}/{bath_ids.length}</p>
        {:then events}
            <EventsList name="Today" events={
                events.filter(e => e.date === today && allowed_states.includes(e.state)).sort(eventSorter)
            }/>
            <EventsList name="Later Dates" events={
                events.filter(e => e.date > today && allowed_states.includes(e.state))
            }/>
            
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