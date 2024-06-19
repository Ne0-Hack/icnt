<script setup>

</script>

<template>
	<div class="flex flex-col gap-[20px] items-center w-[100px]">
		<svg class="spinner" width="50" height="50" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
			<mask id="path-1-inside-1_1039_680" fill="white">
				<path d="M0 50C0 22.3858 22.3858 0 50 0V0C77.6142 0 100 22.3858 100 50V50C100 77.6142 77.6142 100 50 100V100C22.3858 100 0 77.6142 0 50V50Z"/>
			</mask>
			<path d="M0 49C0 20.8335 22.8335 -2 51 -2C79.1665 -2 102 20.8335 102 49L98 50C98 23.4903 76.5097 2 50 2C22.3858 2 0 23.4903 0 50V49ZM100 100H0H100ZM0 100V0V100ZM51 -2C79.1665 -2 102 20.8335 102 49C102 77.1665 79.1665 100 51 100H50C76.5097 100 98 77.6142 98 50C98 23.4903 76.5097 2 50 2L51 -2Z" fill="#BCFF00" mask="url(#path-1-inside-1_1039_680)"/>
		</svg>
		<span class="text-[14px] font-bold">Загрузка</span>
	</div>
</template>

<style>
	@keyframes rotate {
		0% {
			transform: rotate(0deg);
		}
		100% {
			transform: rotate(360deg);
		}
	}
	.spinner {
		display: block;
		animation: rotate .5s infinite linear;
	}
</style>