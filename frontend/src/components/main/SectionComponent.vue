<script setup>

</script>

<template>
	<section>
		<div class="container">
			<div class="section-header mt-[170px] flex">
				<h2 class="w-full text-yellow font-extrabold text-[40px] leading-[76px] uppercase">
					<slot name="title"></slot>
				</h2>
				<slot name="header"></slot>
			</div>
			<div class="section-body mt-[42px]">
				<slot name="content"></slot>
			</div>
			<div class="section-footer mt-[62px] flex justify-center">
				<slot name="footer"></slot>
			</div>
		</div>
	</section>
</template>

<style>

.section-header {
	display: flex;
}

.section-body {

}

.section-footer {

}

</style>