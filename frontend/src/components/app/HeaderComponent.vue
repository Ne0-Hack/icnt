<script setup>
	import ImageComponent from "@components/app/ImageComponent.vue";

	const props = defineProps({
		img: {
			type: String,
			default: () => {
				return null
			}
		}
	})
</script>

<template>
	<div class="w-full h-[788px] flex flex-col justify-center items-center text-light px-[14px]">
		<ImageComponent :img="props.img" object-fit="cover" :blackout="true" radius="20px" width="calc(100% - 28px)" height="788px"  class="absolute -z-10"></ImageComponent>
		<h1 class="text-[80px] font-extrabold leading-[79.2px] tracking-wide text-center w-[1100px]">
			<slot name="title"></slot>
		</h1>
		<h3 class="mt-[45px] text-[20px] font-manrope font-semibold leading-[22.2px] tracking-wide text-center w-[570px]">
			<slot name="subtitle"></slot>
		</h3>
	</div>
</template>