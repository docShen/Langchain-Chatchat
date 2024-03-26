import os


# 默认选用的 LLM 名称
DEFAULT_LLM_MODEL = "qwen"

# 默认选用的 Embedding 名称
DEFAULT_EMBEDDING_MODEL = "bge"


# AgentLM模型的名称 (可以不指定，指定之后就锁定进入Agent之后的Chain的模型，不指定就是LLM_MODELS[0])
Agent_MODEL = None

# 历史对话轮数
HISTORY_LEN = 3

# 大模型最长支持的长度，如果不填写，则使用模型默认的最大长度，如果填写，则为用户设定的最大长度
MAX_TOKENS = None

# LLM通用对话参数
TEMPERATURE = 0.7
# TOP_P = 0.95 # ChatOpenAI暂不支持该参数

SUPPORT_AGENT_MODELS = [
    "chatglm3-6b",
    "openai-api",
    "Qwen-14B-Chat",
    "Qwen-7B-Chat",
    "qwen",
]


LLM_MODEL_CONFIG = {
    # 意图识别不需要输出，模型后台知道就行
    "preprocess_model": {
        DEFAULT_LLM_MODEL: {
            "temperature": 0.05,
            "max_tokens": 4096,
            "history_len": 100,
            "prompt_name": "default",
            "callbacks": False
        },
    },
    "llm_model": {
        DEFAULT_LLM_MODEL: {
            "temperature": 0.9,
            "max_tokens": 4096,
            "history_len": 10,
            "prompt_name": "default",
            "callbacks": True
        },
    },
    "action_model": {
        DEFAULT_LLM_MODEL: {
            "temperature": 0.01,
            "max_tokens": 4096,
            "callbacks": True
        },
    },
    "postprocess_model": {
        DEFAULT_LLM_MODEL: {
            "temperature": 0.01,
            "max_tokens": 4096,
            "prompt_name": "default",
            "callbacks": True
        }
    },
    "image_model": {
        "sd-turbo": {
            "size": "256*256",
        }
    },
    "multimodal_model": {
        "qwen-vl": {}
    },
}

# 可以通过 loom/xinference/oneapi/fastchat 启动模型服务，然后将其 URL 和 KEY 配置过来即可。
#   - platform_name 可以任意填写，不要重复即可
#   - platform_type 可选：openai, xinference, oneapi, fastchat。以后可能根据平台类型做一些功能区分
#   - 将框架部署的模型填写到对应列表即可。不同框架可以加载同名模型，项目会自动做负载均衡。

MODEL_PLATFORMS = [
    # {
    #     "platform_name": "openai-api",
    #     "platform_type": "openai",
    #     "api_base_url": "https://api.openai.com/v1",
    #     "api_key": "sk-yBuaCpqEVUBarBP9700e7224A2D743AeA329334d19C0A336",
    #     "api_proxy": "https://qujhzynu.cloud.sealos.io/v1",
    #     "api_concurrencies": 5,
    #     "llm_models": [
    #         "gpt-3.5-turbo",
    #     ],
    #     "embed_models": [],
    #     "image_models": [],
    #     "multimodal_models": [],
    # },

    {
        "platform_name": "xinference",
        "platform_type": "xinference",
        "api_base_url": "http://127.0.0.1:9997/v1",
        "api_key": "EMPTY",
        "api_concurrencies": 5,
        # 注意：这里填写的是 xinference 部署的模型 UID，而非模型名称
        "llm_models": [
            "qwen",
            "glm3",
        ],
        "embed_models": [
            "bge",
        ],
        "image_models": [
            "sd-turbo",
        ],
        "multimodal_models": [
            "qwen-vl",
        ],
    },

    {
        "platform_name": "oneapi",
        "platform_type": "oneapi",
        "api_base_url": "http://127.0.0.1:3000/v1",
        "api_key": "sk-Mlft68FXoTYqLfQr06F0E2D77e6e4220B6F420999d25383f",
        "api_concurrencies": 5,
        "llm_models": [
            # 智谱 API
            "chatglm_pro",
            "chatglm_turbo",
            "chatglm_std",
            "chatglm_lite",
            # 千问 API
            "qwen-turbo",
            "qwen-plus",
            "qwen-max",
            "qwen-max-longcontext",
            # 千帆 API
            "ERNIE-Bot",
            "ERNIE-Bot-turbo",
            "ERNIE-Bot-4",
            # 星火 API
            "SparkDesk",
        ],
        "embed_models": [
            # 千问 API
            "text-embedding-v1",
            # 千帆 API
            "Embedding-V1",
        ],
        "image_models": [],
        "multimodal_models": [],
    },

    # {
    #     "platform_name": "loom",
    #     "platform_type": "loom",
    #     "api_base_url": "http://127.0.0.1:7860/v1",
    #     "api_key": "88296d2f9bbd9ab222c1086e39f5fbb2.FbC0YSrAMcaEF2gB",
    #     "api_concurrencies": 5,
    #     "llm_models": [
    #         "chatglm3-6b",
    #     ],
    #     "embed_models": [],
    #     "image_models": [],
    #     "multimodal_models": [],
    # },
]

LOOM_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "loom.yaml")
