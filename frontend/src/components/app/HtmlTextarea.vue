<script setup>
const props = defineProps({
	html: {
		type: String,
		default: () => {
			return ""
		}
	}
})
</script>

<template>
	<div class="text-area" v-html="props.html"></div>
</template>

<style>
.text-area {
	@apply font-manrope;
}
.text-area h1 {
	@apply text-[40px] font-raleway font-bold text-yellow mb-[32px] pt-[68px]
}
.text-area h1:first-child {
	@apply -mt-[68px];
}
.text-area h2 {
	@apply text-[20px] uppercase font-raleway font-bold text-yellow mb-[20px] pt-[45px];
}
.text-area h2:first-child {
	@apply -mt-[45px];
}
.text-area p {

}
.text-area ol {
	@apply list-decimal pl-4 text-[16px] flex flex-col gap-[16px];
}
.text-area ul {
	@apply list-disc pl-4 text-[16px] flex flex-col gap-[16px];
}

.text-area img {
	@apply mt-[25px];
}

</style>