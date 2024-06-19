<script setup>
import {reactive, toRef} from "vue";

const props = defineProps({
	placehloder: {
		type: String,
		default: () => {
			return ""
		}
	},
	width: {
		type: String,
		default: () => {
			return '400px'
		}
	},
	type: {
		type: String,
		default: () => {
			return "text"
		}
	},
	value: {
		type: String,
		default: () => {
			return ""
		}
	},
	name: {
		type: String,
		default: () => {
			return ''
		}
	},
	error: {
		type: Array,
		default: () => {
			return []
		}
	},
	theme: {
		type: String,
		default: () => {
			return 'dark'
		}
	},
	label: {
		type: String,
		default: () => {
			return ''
		}
	},
	disabled: {
		type: Boolean,
		default: () => {
			return false
		}
	}
})
const emits = defineEmits(["onInput"])

const state = reactive({
	value: props.value,
	error: toRef(() => props.error),
})

</script>

<template>
	<div class="relative"
		:class="{
					'theme-dark': props.theme === 'dark',
					'theme-light': props.theme === 'light',
		}"
	>
		<label class="label"
				v-if="props.label.length > 0">
			{{ props.label }}
		</label>
		<input
				class="input-component"
				:class="{
					'danger': state.error.length !== 0,
				}"
				:style="{
					'width': props.width
				}"
				:placeholder="props.placehloder"
				:type="props.type"
				:name="props.name"
				:disabled="props.disabled"
				v-model="state.value"
				@input="emits('onInput', state.value)"
		/>
		<ul v-show="state.error.length !== 0"
				 class="text-danger mt-[3px] absolute top-[100%]"
		>
			<li v-for="val of state.error">
				{{ val }}
			</li>
		</ul>
	</div>
</template>

<style scoped>
	.input-component {
		@apply rounded-[8px] outline-none border-[1px] border-[transparent] h-[50px] px-[20px]
		text-[14px] font-manrope leading-[16.3px] transition-colors
	}
	.label {
		@apply block font-raleway text-[18px] leading-[32px] font-medium
	}

	.theme-dark > .input-component {
		@apply bg-[#141414] text-light;
		color-scheme: dark;
	}
	.theme-dark > .input-component::placeholder {
		@apply opacity-50
	}
	.theme-dark > .label {
		@apply text-light
	}

	.theme-light > .input-component {
		@apply bg-[#FFFFFF] text-dark border-dark border-opacity-[12%]
	}
	.theme-light > .input-component::placeholder {
		@apply text-dark opacity-50
	}
	.theme-light > .label {
		@apply text-dark
	}

	.input-component:focus {
		@apply border-yellow bg-opacity-10 caret-yellow;
		box-shadow: 0 0 30px 0 #BCFF0026;

	}
	.input-component.danger {
		@apply border-danger
	}
</style>