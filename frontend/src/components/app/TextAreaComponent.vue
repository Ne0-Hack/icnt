<script setup>
import {reactive, toRef} from "vue";

const props = defineProps({
	placehloder: {
		type: String,
		default: () => {
			return ""
		}
	},
	value: {
		type: String,
		default: () => {
			return ""
		}
	},
	rows: {
		type: String,
		default: () => {
			return '3'
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
		<textarea
				class="textarea-component"
				:class="{
					'danger': state.error.length !== 0,
				}"
				:rows="props.rows"
				:placeholder="props.placehloder"
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
	.textarea-component {
		@apply rounded-[8px] outline-none border-[1px] border-[transparent] w-full px-[20px] py-[18px]
		text-[14px] font-manrope leading-[16.3px] transition-colors
	}
	.label {
		@apply block font-raleway text-[18px] leading-[32px] font-medium
	}

	.theme-dark > .textarea-component {
		@apply bg-[#141414] text-light
	}
	.theme-dark > .textarea-component::placeholder {
		@apply opacity-50
	}
	.theme-dark > .label {
		@apply text-light
	}

	.theme-light > .textarea-component {
		@apply bg-[#FFFFFF] text-dark border-dark border-opacity-[12%]
	}
	.theme-light > .textarea-component::placeholder {
		@apply text-dark opacity-50
	}
	.theme-light > .label {
		@apply text-dark
	}

	.textarea-component:focus {
		@apply border-yellow bg-opacity-10 caret-yellow;
		box-shadow: 0 0 30px 0 #BCFF0026;

	}
	.textarea-component.danger {
		@apply border-danger
	}
</style>