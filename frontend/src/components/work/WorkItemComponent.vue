<script setup>

import ImageComponent from "@components/app/ImageComponent.vue";

const props = defineProps({
	imageA: {
		type: String,
		default: () => {
			return null
		}
	},
	imageB: {
		type: String,
		default: () => {
			return null
		}
	},
	category: {
		type: String,
		default: () => {
			return "No category"
		}
	},
	title: {
		type: String,
		default: () => {
			return "No title"
		}
	},
	checklist: {
		type: Array,
		default: () => {
			return []
		}
	},
	reverse: {
		type: Boolean,
		default: () => {
			return false
		}
	}
})

</script>

<template>
	<div class="flex gap-[140px] pt-[62px]"
			:class="{'flex-row-reverse': props.reverse}">
		<div class="w-[764px] h-[380px] block overflow-hidden relative">
			<ImageComponent class="absolute -bottom-[50px]" :class="{'left-0': !props.reverse, 'right-0': props.reverse}"
					:img="imageB" object-fit="cover" width="594px" height="320px" radius="20px" />
			<ImageComponent class="absolute top-0" :class="{'right-0': !props.reverse, 'left-0': props.reverse}"
					:img="imageA" object-fit="cover" width="594px" height="399px" radius="20px" />
		</div>
		<div class="flex flex-col">
			<div class="font-semibold text-[20px] leading-[19.8px] tracking-[5%]">
				{{ props.category }}
			</div>
			<div class="mt-[10px] font-extrabold text-[30px] leading-[29.8px] tracking-[5%]">
				{{ props.title }}
			</div>
			<div class="mt-[25px] flex flex-col gap-[17px] w-[310px]">
				<div v-for="i in props.checklist"
						 class="flex items-start gap-[10px]">
					<span>
						<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"
								 xmlns:xlink="http://www.w3.org/1999/xlink">
							<rect width="20" height="20" fill="url(#pattern0_3_105)"/>
							<defs>
							<pattern id="pattern0_3_105" patternContentUnits="objectBoundingBox" width="1" height="1">
							<use xlink:href="#image0_3_105" transform="scale(0.03125)"/>
							</pattern>
							<image id="image0_3_105" width="32" height="32"
										 xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAASZSURBVFiFrddtbJ5lFQfw37n7sjl0bhNfEPAFgxqIiMqMEiBufVpkJqgRSXTRaGAqGj4wEZUQnRKNETTOoHF8mC8Z0QyICWqTrk9bYB0aGTH7AEZJiGHCRnRbnRGhpc/xw3097bPRdt3s/8t9X+f63+f/v9+uc66wSAymZcvpa7EeF+ANWI2p4FByAL8P9rycsYvC1GLyxokII+nMZDM+XQQXg4PBzyq2rgsHT8nA3tRzhC8HN+MlHVPTeBT78QymcDrOxfno6uAeDW6t+MG68EI7mCnGuGKKP3fPJT6Wzprg7uA9HeHd+Pkk920I/5jrusG0spcrsQmXYWVy23R9A7e2eSPchi928eSLnsBoekuLXXhdCT2W3NQffjeX6Hxopga24rzgur7wkxLfiB2F9tAxBobS2V3swdmQ/PI0rrk4/PdkxNvYkqpLOaMvPAUj6Z3JuPqJ/LOLtTMGdqbeNfXk2hL6dh+3RMhTET8eg+mVvTyM1+MFDDTCWNUmrOGWDvG7llJ8b+rpZWcRhxsbYQwqGEpvxE1lcl8X1y6VOPyL7+F9ZfiLRtjanqugmy9hWdvduvDcUomPpE8l15fh3i4+2zkfQ+m0Lg7ipRhuhIElFH938gCW45lp1l4e9ndyuis+UMRh+1KJj6XXTHNvEZ8Krm6LN9M38MHkExXWlWsmJxk8PtHe1HOy4jtT7zR346wSuqEvPNhB+QLejs9UwYUl+McN4WibkSmG0/gEh0bTlSdjYHW9AF1Shtsb4UfHUf5Sju+ogjeVwd87GY/QHXXVe1mLe0bSxxYjPpw2BZ8rwz9M8vk5aI9BcE6VrCyDA52Mi8JU8lE8i55kx3DatJD4SLo4uKMMD7T4yIbw/BzUw+W4qlJ+xVZd5Y5BfxgKrsBRVMG24XTDXOK70muTe9CLyeCqgfD0PF7ba0xUJbngjLmY5eNpFNcRfH8kfb2TM5iWVfUX385xfV94aB5x6vINhyr8rQzOnI/dCA9nvZIdLPa3NNPtmXU/0cuPzZbubY1w5wLi1L0DPB3DaXvU3c6zKzh9ocq3K51b0TRbqu9SNyWbi7E9R1h/dZicL8fe1DPBBFYkd1S4v8yteI7+hWwPhMeTS/F4CW1si+Opbq5aSByOMIAVEIxXy/kN9Zfa4pMLXQz94Um1id923lhF34n6vyJ6bTn993Q7RzPtaKZsplYzZ0ryCdFMrxjKunlZDEbTu5ppumhtK4YYTee32KduKB88XL/HF/2W/y+aaVS99D+P8xrhiQrWh0epezZctprvLLV4wQXl+MNGeIKyCEEXX8FfIbixmcfW7aVAxeXBdYfr7kvRmkV5FbvNbkC+O85Xt4TWUpuZ0wA003vVZXlVCd2fbO4PfzqZxM30ZmysuG99eGTRBmA4vS34tdlK2Qp+lfx0FQ/Mt+8rbfglyTX4OLqxrxEzJX9xBqh3Ocu4vSSrOqYmMB7sz3ppnkrWBG9Vd9Wv7uC2gq/1hW+dtIE2ymbiZnzIsfu+hTCpfoLfbERd+0/ZQBtD6VVdfFj9H1+Ic5hp1/4T7G/VG4/d09z7/pip+Qvif7ekclLXf51ZAAAAAElFTkSuQmCC"/>
							</defs>
						</svg>
					</span>
					{{ i }}
				</div>
			</div>
		</div>
	</div>
</template>