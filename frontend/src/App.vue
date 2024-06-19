<script setup>
import NavbarComponent from "@components/app/navigation/NavbarComponent.vue";
import FooterComponent from "@components/app/navigation/FooterComponent.vue";
</script>

<template>
	<div class="flex flex-col min-h-[100dvh]">
		<NavbarComponent />
		<router-view style="flex: 1 1 auto;"></router-view>
	</div>
	<FooterComponent style="flex: 0 0 auto"  />

</template>
