def create_promptbook(gr):
	with gr.Blocks(analytics_enabled=False) as pb:
		with gr.Tabs(elem_id='prompt_tabs'):
			open_promptbook(gr)
			open_prompt_tab(gr, "fire")
			open_prompt_tab(gr, "potato")
	return pb


def open_promptbook(gr):
	with gr.Tab("promptbook"):
		with gr.Blocks(analytics_enabled=False):
			with gr.Row():
				renew_page = gr.Button('Renew Page')
				first_page = gr.Button('First Page')
				prev_page = gr.Button('Prev Page')
				page_index = gr.Number(value=1, label="Page Index")
				next_page = gr.Button('Next Page')
				end_page = gr.Button('Last Page')
			with gr.Row():
				with gr.Row():
					with gr.Column(scale=3):
						prompt_gallery = gr.Gallery(show_label=False).style(grid=6)
						with gr.Row():
							process_queue = gr.Button('Process queue', variant='primary')  # TODO Button change to cancel / back
							prio_up = gr.Button('Priority Up')
							prio_down = gr.Button('Priority Down')
						with gr.Row():
							gr.components.Textbox(interactive=False, value="14 seeds / 2 prompts / 2 models", label="Queue")  # TODO Could be a progressbar
							per_prompt_num = gr.Slider(minimum=1, maximum=1000, step=1, value=100, interactive=True, label="Cycle prompts after at most")
							per_model_num = gr.Slider(minimum=1, maximum=10000, step=1, value=-1, interactive=True, label="Cycle models after at most")
					with gr.Column():
						with gr.Row():
							add_prompt = gr.Button('Add (txt2img)', variant='primary')
							edit_txt2img = gr.Button('Edit (txt2img)')
						with gr.Row(label="Toggles"):
							generate_all = gr.Button('Generate All')  # TODO Use single persistent flag on the queuelist for the whole prompt rather than adding/removing seeds!
							pause_prompt = gr.Button('Pause')  # TODO button change to cancel and back


# TODO Major: Opening a new tab based on a prompt may not be supported by Gradio?
def open_prompt_tab(gr, seedname: str):
	with gr.Tab(seedname):
		with gr.Row():
			renew_page = gr.Button('Renew Page')
			first_page = gr.Button('First Page')
			prev_page = gr.Button('Prev Page')
			page_index = gr.Number(value=1, label="Page Index")
			next_page = gr.Button('Next Page')
			end_page = gr.Button('Last Page')
		with gr.Row():
			with gr.Column(scale=3):
				seed_gallery = gr.Gallery(show_label=False).style(grid=2)
				with gr.Row():
					delete_num = gr.Number(value=1, interactive=True, label="number of seeds/images to delete consecutively")
					delete = gr.Button('Delete Selected')
			with gr.Column():
				with gr.Row():
					add_seed = gr.Button('Add Seeds', variant='primary')
					add_seed_num = gr.Slider(minimum=1, maximum=50, step=1, value=5, interactive=True, label="Amount")
				with gr.Row():
					with gr.Column(min_width=160):
						seed_num = gr.Number(value=-1, interactive=True, label="Seed")
					with gr.Column(min_width=80):
						sequential_checkbox = gr.Checkbox(value=True, interactive=True, label="Seq(+1 each)")
						generate_checkbox = gr.Checkbox(value=True, interactive=True, label="Generate")
				with gr.Row():
					mark_generation = gr.Button('Toggle Generate', variant='primary')
					edit_txt2img = gr.Button('Edit Seed (txt2img)')  # TODO Restrict to one OR ensure same settings except the seed number
				with gr.Row():
					edit_img2img = gr.Button('Images to img2img')
					edit_extra = gr.Button('Images to Extras')  # TODO Multiple seeds could be edited if they had the same settings except seed_num?
				with gr.Row():
					delete_to_seed = gr.Button('Add Seeds & Delete Images', interactive=False)
