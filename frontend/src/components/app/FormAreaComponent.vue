<script setup>
import ImageComponent from "@components/app/ImageComponent.vue";
import Logo from "@images/logo_light.svg"
const props = defineProps({
	cols: {
		type: String,
		default: () => {
			return '1'
		}
	},
	rows: {
		type: String,
		default: () => {
			return '1'
		}
	},
	submitText: {
		type: String,
		default: () => {
			return "Отправить"
		}
	},
	logo: {
		type: Boolean,
		default: () => {
			return true
		}
	},
	theme: {
		type: String,
		default: () => {
			return 'dark'
		}
	},
	padding: {
		type: String,
		default: () => {
			return '25px'
		}
	},
	flowCol: {
		type: Boolean,
		default: () => {
			return false
		}
	}
})

const emits = defineEmits(["onSubmit"])

const bodyStyle = {
	'grid-template-columns': `repeat(${props.cols}, minmax(0, 1fr))`,
	'grid-template-rows': `repeat(${props.rows}, minmax(0, 1fr))`,
}
</script>

<template>
	<form
			@submit.prevent="emits('onSubmit')"
			class="form"
			:style="{
				'padding-left': props.padding,
				'padding-right': props.padding

			}"
			:class="{
					'theme-dark': props.theme === 'dark',
					'theme-light': props.theme === 'light',
				}"
	>
		<div v-if="props.logo" class="">
			<ImageComponent :img="Logo" width="124px" height="28px" />
		</div>
		<div class="mt-[50px] text-light text-[25px] leading-[29.3px] font-[500]">
			<slot name="title"></slot>
		</div>
		<div class="mt-[20px] grid gap-[25px]"
				 :class="{
						'grid-flow-col': props.flowCol
				 }"
				 :style="bodyStyle"
				 >
			<slot name="body"></slot>
		</div>
		<div class="mt-[20px] text-center text-danger">
			<slot name="error"></slot>
		</div>
		<div class="mt-[30px] text-center">
			<slot name="submit">
				<button type="submit" class="w-[400px] h-[50px] ">
					{{ props.submitText }}
				</button>
			</slot>
		</div>
		<div class="mt-[25px] text-[14px] font-manrope leading-[19.1px] text-center">
			<slot name="footer"></slot>
		</div>
	</form>
</template>

<style>

.form {
	@apply py-[25px] rounded-[10px]
}

.form.theme-dark {
	@apply bg-[#1C1C1C] text-light
}

.form.theme-light {
	@apply bg-[#FFFFFF] text-dark
}
</style>