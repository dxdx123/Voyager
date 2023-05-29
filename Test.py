from voyager import Voyager

# you can also use mc_port instead of azure_login, but azure_login is highly recommended
azure_login = {
    "client_id": "36511da7-b36f-4f77-81d5-19af07dbf747",
    "redirect_url": "https://127.0.0.1/auth-response",
    "secret_value": "",
    "version": "fabric-loader-0.14.18-1.19", # the version Voyager is tested on
}
openai_api_key = "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"

voyager = Voyager(
    azure_login=azure_login,
    openai_api_key=openai_api_key,
)

# start lifelong learning
voyager.learn()