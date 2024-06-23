<script setup>
import ImageComponent from "@components/app/ImageComponent.vue";

const props = defineProps({
	tags: {
		type: Array,
		default: () => {
			return []
		}
	},
	img: {
		type: String,
		default: () => {
			return null
		}
	}
})

</script>

<template>
	<div class="flex flex-col w-[590px]">
		<ImageComponent :img="props.img" width="100%" height="378px" object-fit="cover" radius="14px"/>
		<div class="mt-[20px] flex flex-wrap gap-[10px] opacity-70">
			<div v-for="i in props.tags"
					 class="flex border rounded-[50px] px-[11px] py-[5px] font-urbanist text-[14px] leading-[21.5px] tracking-[2.5%]">
				{{ i }}
			</div>
		</div>
	</div>
</template>
