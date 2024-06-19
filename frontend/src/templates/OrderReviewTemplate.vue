<script setup>
import FormComponent from "@components/app/FormAreaComponent.vue";
import InputComponent from "@components/app/InputComponent.vue";
import SelectComponent from "@components/app/SelectComponent.vue";
import TextAreaComponent from "@components/app/TextAreaComponent.vue";
import {reactive} from "vue";
import {useRouter} from "vue-router";
import axios from "axios";

const router = useRouter()

const sendReview = () => {
	state.errors = []
	axios.post("http://127.0.0.1:8000/contents/reviews/", {
		"title": state.form.title,
		"text": state.form.text,
	})
			.then((e) => {

				if (e.status === 201) {
					router.push({name: 'profile'})
				}
			})
			.catch((e) => {
				if (e.response) {
					state.errors = e.response.data
				}  else {
					state.errors.push({'non_field_errors': ["Ошибка сервера"]})
				}
			})
}

const state = reactive({
	errors: [],
	form: {
		title: '',
		text: '',
	}
})


</script>

<template>
	<div class="flex justify-center items-center">
		<div class="container">
			<FormComponent
					:flow-col="false"
					@onSubmit="sendReview"
					submit-text="Отправить отзыв"
			>
				<template #title>Оставить отзыв</template>
				<template #body>
					<InputComponent @onInput="(e) => state.form.title = e" width="100%" placehloder="Введите заголовок, например кейтеринг для ресторана" :error="state.errors['title']" />
					<TextAreaComponent @onInput="(e) => state.form.text = e" rows="6" placehloder="Введите текст вашего отзыва" :error="state.errors['text']"/>

				</template>
				<template #error>
					<span v-for="val of state.errors['non_field_errors']">
					{{ val }}
					</span>
				</template>
			</FormComponent>
		</div>
	</div>

</template>