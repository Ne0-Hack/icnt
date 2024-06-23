<script setup>
import HeaderComponent from "@components/app/HeaderComponent.vue";
import SectionComponent from "@components/main/SectionComponent.vue";
import WorkItemComponent from "@components/work/WorkItemComponent.vue";
import {onBeforeMount, reactive} from "vue";
import axios from "axios";
import WorksImg from "@images/works.png"


const state = reactive({
	works: []
})

const loadWorks = async () => {
	const res = await  axios.get(`${import.meta.env.VITE_API_ENDPOINT}/contents/works/`)
	if (res.status === 200) {
		state.works = res.data
	}
}

onBeforeMount(async () => {
	await loadWorks()
})


</script>

<template>
	<HeaderComponent :img="WorksImg">
		<template #title>Портфолио собранное нами за всё время</template>
	</HeaderComponent>
	<SectionComponent>
		<template #content>
			<WorkItemComponent
				v-for="(val, key) in state.works"
				:category="val.subtitle"
				:title="val.title"
				:checklist="val.tasks"
				:image-a="val.imageA"
				:image-b="val.imageB"
				:reverse="key % 2 === 0"
			/>
		</template>
	</SectionComponent>
</template>