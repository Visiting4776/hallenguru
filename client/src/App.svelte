<script>
	import { onMount } from 'svelte';
	import Event from "./components/Event.svelte";
	
	let events = [];
	onMount(async () => {
		const res = await fetch("./get_bath_info");
		events = await res.json();
	});
	// function getBaths() {
	// 	fetch("./get_bath_info")
	// 		.then(d => d.text())
	// 		.then(d => (events = JSON.parse(d)));
	// }
</script>

<main>
	<h1>Hello!</h1>

	{#each events as event}
		<Event {event}/>
	{/each}
</main>
