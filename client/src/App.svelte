<script>
	import { onMount } from 'svelte';
	import Event from "./components/Event.svelte";
	
	let events = [
  {
    "bath_id": 1, 
    "date": "Fri, 25 Feb 2022 00:00:00 GMT", 
    "end_time": "19:45", 
    "from_date": "", 
    "name": "Stadtbad Mitte", 
    "start_time": "17:45", 
    "state": "reserved"
  }, 
  {
    "bath_id": 1, 
    "date": "Fri, 25 Feb 2022 00:00:00 GMT", 
    "end_time": "22:00", 
    "from_date": "", 
    "name": "Stadtbad Mitte", 
    "start_time": "20:00", 
    "state": "soldout"
  }, 
  {
    "bath_id": 1, 
    "date": "Sat, 26 Feb 2022 00:00:00 GMT", 
    "end_time": "08:30", 
    "from_date": "", 
    "name": "Stadtbad Mitte", 
    "start_time": "06:30", 
    "state": "soldout"
  }, 
  {
    "bath_id": 1, 
    "date": "Sat, 26 Feb 2022 00:00:00 GMT", 
    "end_time": "10:45", 
    "from_date": "", 
    "name": "Stadtbad Mitte", 
    "start_time": "08:45", 
    "state": "soldout"
  }, 
  {
    "bath_id": 1, 
    "date": "Sat, 26 Feb 2022 00:00:00 GMT", 
    "end_time": "13:00", 
    "from_date": "", 
    "name": "Stadtbad Mitte", 
    "start_time": "11:00", 
    "state": "soldout"
  }, 
  {
    "bath_id": 1, 
    "date": "Sat, 26 Feb 2022 00:00:00 GMT", 
    "end_time": "15:15", 
    "from_date": "", 
    "name": "Stadtbad Mitte", 
    "start_time": "13:15", 
    "state": "soldout"
  }, 
  {
    "bath_id": 1, 
    "date": "Sat, 26 Feb 2022 00:00:00 GMT", 
    "end_time": "17:30", 
    "from_date": "", 
    "name": "Stadtbad Mitte", 
    "start_time": "15:30", 
    "state": "soldout"
  },
];
	// onMount(async () => {
	// 	const res = await fetch("./get_bath_info");
	// 	events = await res.json();
	// });
	// function getBaths() {
	// 	fetch("./get_bath_info")
	// 		.then(d => d.text())
	// 		.then(d => (events = JSON.parse(d)));
	// }
</script>

<div class="mt-2 mx-auto max-w-xl bg-white shadow-md px-3 py-5">
<h1>Today</h1>
<div class="space-y-3 divide-y divide-solid">
	{#each events as event}
		<Event {event}/>
	{/each}
</div>
</div>

<style global lang="postcss">
	@tailwind base;
	/* @tailwind components; */
	@tailwind utilities;
  </style>