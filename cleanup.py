from huggingface_hub import scan_cache_dir

cache_info = scan_cache_dir()

delete_strategy = scan_cache_dir().delete_revisions(
    "4643665f84c6760e3cbf6adaace6c398592270af",
    "0fc9ddf78a1e988dac52e2dac162b0ede4fd74ab"
)

delete_strategy.execute()
