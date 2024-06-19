<script setup>
import HeaderComponent from "@components/app/HeaderComponent.vue";
import header_img from "@images/main_header.png"
import ServicesSectionTemplate from "@templates/main/ServicesSectionTemplate.vue";
import NewsSectionTemplate from "@templates/main/NewsSectionTemplate.vue";
import AboutSectionTemplate from "@templates/main/AboutSectionTemplate.vue";
import WorksSectionTemplate from "@templates/main/WorksSectionTemplate.vue";
import ReviewsSectionTemplate from "@templates/main/ReviewsSectionTemplate.vue";
</script>

<template>
	<HeaderComponent :img="header_img">
		<template #title>Инжиниринговый центр новых технологий</template>
		<template #subtitle>Объединяем образование и инновации для создания лучшего будущего</template>
	</HeaderComponent>
	<AboutSectionTemplate id="about" />
	<ServicesSectionTemplate id="services" />
	<ReviewsSectionTemplate id="reviews" />
	<WorksSectionTemplate id="works" />
	<NewsSectionTemplate id="news" />
</template>