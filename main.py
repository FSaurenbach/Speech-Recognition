import torchaudio
train_dataset = torchaudio.datasets.LIBRISPEECH("./", url="train-clean-100", download=True)
test_dataset = torchaudio.datasets.LIBRISPEECH("./", url="test-clean", download=True)
torchaudio.transforms.FrequencyMasking()
torchaudio.transforms.TimeMasking()