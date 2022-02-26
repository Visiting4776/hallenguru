<script>
    export let event;
</script>

<div class="pt-3">
    <div class="flex flex-row items-center justify-between">
        <div> <!-- Event details -->
            <div class="font-light">{event.name} {#if event.state === 'reserved'}({event.state}){/if}</div>
            <div class="text-xl tracking-tight">{event.start_time} - {event.end_time}</div>
        </div>
        <a href='{event.link}'><button class="px-1 py-1 text-white transition-all duration-100 bg-green-600 border-2 border-green-600 shadow 
        active:bg-green-700 active:border-green-700
        hover:bg-green-500 hover:border-green-500 hover:shadow-none
        disabled:border-gray-200 disabled:border-2 disabled:bg-transparent disabled:shadow-none"
        disabled={event.state!='available'}>Book Now</button></a>
    </div>
</div>