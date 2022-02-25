<script>
    export let event;
</script>

<div class="pt-3">
    <div class="flex flex-row items-center justify-between">
        <div> <!-- Event details -->
            <div class="font-light opacity-80">{event.name}</div>
            <div class="text-xl tracking-tight">{event.start_time} - {event.end_time}</div>
        </div>
        <a href='#'><button class="px-2 py-2 text-white transition-all duration-100 bg-green-600 border-none shadow 
        active:bg-green-700 
        hover:bg-green-500 hover:shadow-none">Book Now</button></a>
    </div>
</div>