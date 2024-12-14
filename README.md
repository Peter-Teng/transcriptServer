# Transcript Server
A simple transcript (ASR) server based on Python (3.9.20), using Flask (web server), fsmn-vad, sensevoice-small (speech transcription) and cam++ (speaker verification). It can register speaker, then transcripts audio while identify the specific speaker.

---
## Quick Start
``` shell
git clone git@github.com:Peter-Teng/transcriptServer.git
cd transcriptServer
# Using Anaconda
conda create -n transcriptServer python=3.9
conda activate transcriptServer
# Installing requirements
pip install -r requirements.txt
```
Downloading the models is required when starting the application for the first time (this may take a few minutes). Then the web service should be able to work offline.


The default host is *localhost*, and the server will serve at port *8000* (host and port could be changed).
``` shell
python app.py --download
```

## Usage
The server contains two APIs. **"/transcript"** is for transcripting a certain audio file (only support .wav currently). **"/register"** is for registing a speaker to the server in order to be recognized.


Here is a basic example, the example audio files could be found at the folder *example*.
```shell
# /register
curl --location --request POST "localhost:8000/register" ^
--header "Content-Type: application/json" ^
--data-raw "{ \"path\": \"{your_path}/examples/customer.wav\", \"speaker\": \"customer\"}"

# /transcript
curl --location --request POST "localhost:8000/transcript" ^
--header "Content-Type: application/json" ^
--data-raw "{\"path\": \"{your_path}/examples/customer_service.wav\"}"
```
The result would be:
```json
{
    "code": "0",
    "data": [
        {
            "transcrupt_results": [
                {
                    "content": "Some Sentences",
                    "speaker": "Somebody"
                },
                ...
            ]
        }
    ],
    "describe": "success"
}
```

---

## Reference

```
@inproceedings{gao2023funasr,
  author={Zhifu Gao and Zerui Li and Jiaming Wang and Haoneng Luo and Xian Shi and Mengzhe Chen and Yabin Li and Lingyun Zuo and Zhihao Du and Zhangyu Xiao and Shiliang Zhang},
  title={FunASR: A Fundamental End-to-End Speech Recognition Toolkit},
  year={2023},
  booktitle={INTERSPEECH},
}
@article{an2024funaudiollm,
  title={Funaudiollm: Voice understanding and generation foundation models for natural interaction between humans and llms},
  author={An, Keyu and Chen, Qian and Deng, Chong and Du, Zhihao and Gao, Changfeng and Gao, Zhifu and Gu, Yue and He, Ting and Hu, Hangrui and Hu, Kai and others},
  journal={arXiv preprint arXiv:2407.04051},
  year={2024}
}
@inproceedings{zhang2018deep,
  title={Deep-FSMN for large vocabulary continuous speech recognition},
  author={Zhang, Shiliang and Lei, Ming and Yan, Zhijie and Dai, Lirong},
  booktitle={2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={5869--5873},
  year={2018},
  organization={IEEE}
}
@inproceedings{zheng20233d,
  title={3D-Speaker: A Large-Scale Multi-Device, Multi-Distance, and Multi-Dialect Corpus for Speech Representation Disentanglement},
  author={Siqi Zheng, Luyao Cheng, Yafeng Chen, Hui Wang and Qian Chen},
  url={https://arxiv.org/pdf/2306.15354},
  year={2023}
}
@inproceedings{wang2023cam++,
  title={CAM++: A Fast and Efficient Network For Speaker Verification Using Context-Aware Masking},
  author={Wang, Hui and Zheng, Siqi and Chen, Yafeng and Cheng, Luyao and Chen, Qian},
  booktitle={INTERSPEECH},
  year={2023}
}
```
