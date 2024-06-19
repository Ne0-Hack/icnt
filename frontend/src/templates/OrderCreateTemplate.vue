<script setup>

import FormComponent from "@components/app/FormAreaComponent.vue";
import InputComponent from "@components/app/InputComponent.vue";
import SelectComponent from "@components/app/SelectComponent.vue";
import TextAreaComponent from "@components/app/TextAreaComponent.vue";
import {onBeforeMount, reactive} from "vue";
import {useRouter} from "vue-router";
import axios from "axios";

const router = useRouter()

const sendOrder = () => {
	state.errors = []
	axios.post("http://127.0.0.1:8000/services/order/", {
		"serviceCategory": state.form.serviceCategory,
		"description": state.form.description,
		"deadline": state.form.deadline
	})
			.then((e) => {
				if (e.status === 201) {
					router.push({name: 'profile'})
				}
			})
			.catch((e) => {
				if (e.response) {
					state.errors = e.response.data
				} else {
					state.errors.push({'non_field_errors': ["Ошибка сервера"]})
				}
			})
}

const loadServices = () => {
	axios.get("http://127.0.0.1:8000/services/service")
			.then((e) => {
				state.storage.services = []
				for (let el of e.data) {
					state.storage.services.push({
						id: el['id'],
						title: el['title'],
						category_list: el['category_list']
					})
				}
			})
}

const state = reactive({
	form: {
		service: null,
		serviceCategory: null,
		description: '',
		deadline: null,
	},
	storage: {
		services: []
	},
	errors: []

})

onBeforeMount(() => {
	loadServices()
})


</script>

<template>
	<div class="flex justify-center items-center ">
		<div class="container">
			<FormComponent
					cols="2"
					padding="77px"

			>
				<template #body>
					<SelectComponent @onInput="(e) => state.form.service = e"
													 opt-name="title" opt-id="id"
													 :options="state.storage.services"
													 width="100%"
													 label="Услуга"
													 placehloder="Выберите услугу"/>
					<SelectComponent @onInput="(e) => state.form.serviceCategory = e"
													 :options="state.storage.services.find((e) => e.id === state.form.service)?.category_list"
													 opt-name="title"
													 opt-id="id"
													 :disabled="state.form.service == null"
													 width="100%"
													 label="Тип услуги"
													 placehloder="Выберите тип услуги"
													 :error="state.errors['serviceCategory']"/>
					<InputComponent
							@onInput="(e) => state.form.deadline = e"
							width="100%" label="Срок выполнения"
													placehloder="Выберите срок"
							type="date"
							:error="state.errors['deadline']"/>
					<InputComponent
							width="100%"
							label="Телеграм"
							placehloder="Вставьте ссылку на ваш профиль через @"/>
					<TextAreaComponent
							@onInput="(e) => state.form.description = e"
							class="col-start-1 col-end-3"
							rows="6"
							label="Сообщение" placehloder="Напишите пояснение к заказу здесь"
							:error="state.errors['description']"/>
				</template>
				<template #error>
					<span v-for="val of state.errors['non_field_errors']">
					{{ val }}
					</span>
				</template>
				<template #submit>
					<div class="flex justify-between items-center">
						<button @click="sendOrder" class="uppercase font-semibold px-[35px] bg-[#BCFF00]">
							Отправить заявку
						</button>
						<div class="font-bold uppercase">
							<!--	Стоит бы поправить эту крокозябру на скорую руку, главное не забыть -->
							Сумма: <span>{{ state.storage.services.find((e) => e.id === state.form.service)?.category_list.find((e) => e.id === state.form.serviceCategory)?.price }}</span>
						</div>
					</div>
				</template>
			</FormComponent>
		</div>
	</div>

</template>