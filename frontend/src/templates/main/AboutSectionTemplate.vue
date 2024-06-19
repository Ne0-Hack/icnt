<script setup>
import SectionComponent from "@components/main/SectionComponent.vue";
import AboutComponent from "@components/main/AboutComponent.vue";
</script>

<template>
	<SectionComponent id="about">
		<template #title>О нас</template>
		<template #content>
			<AboutComponent />
		</template>
	</SectionComponent>
</template>

