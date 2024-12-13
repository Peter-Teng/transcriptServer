# Transcript Server
A simple transcript (ASR) server based on Python (3.9.20), using Flask (web server), fsmn-vad, sensevoice-small (speech transcription) and cam++ (speaker verification). It can register speaker, then transcripts audio while identify the specific speaker.

---
## Quick Start
```
git clone git@github.com:Peter-Teng/transcriptServer.git
cd transcriptServer
pip install -r requirements.txt
```
Downloading the models is required when starting the application for the first time (this may take a few minutes). The the web service should be able to work offline.
The default host is *localhost*, and the server will serve at port *8000* (host and port could be changed).
```
python app.py --download
```

## Usage
The server contains two APIs. **"/transcript"** is for transcripting a certain audio file (only support .wav currently). **"/register"** is for registing a speaker to the server in order to be recognized.
Here is a basic example, the example audio files could be found at the folder *example*.
```

```
The result would be:
```
{
    "code": "0",
    "data": [
        {
            "transcrupt_results": [
                {
                    "content": "为您服务。",
                    "speaker": "unknown"
                },
                {
                    "content": "你好，腾讯未成年人家长服务品的专席。请问是哎你好你好，我个问题吗？哎，你好你好，我这这个是我这是前几天申请的那个未成年人退款那个事儿。然后吧，我上网上搜了一下，说必须得给你们客服打电话，才能说尽量的把钱都退回来，是能然后你们那边现在。😊",
                    "speaker": "customer"
                },
                {
                    "content": "是怎么个处理方法呢？现在。",
                    "speaker": "customer"
                },
                {
                    "content": "那就了，先生，您是孩子的哥哥呢，还是孩子本人？我是本人，我现在是呃我那个身份证和我妈啥的，都已经就是跟他沟通了一下，就是已经申请了。",
                    "speaker": "customer"
                },
                {
                    "content": "那姐姐，就是您现在已经提交了退费申请，您想要提一下您的一个退费进度是吧？我就是想跟您跟您说一下，因为我上网上搜了一下，人都说必须得给你们打电话，然后才能那个备注一下也好，是怎么也说也罢，是才能把那个呃90%吧给退回来。",
                    "speaker": "customer"
                },
                {
                    "content": "对我先生并先生并没有这种说法的，并不存在这种说法，请您不要相信其他平台所传的信息，请您以我们的官方答复为准。那你们这个是怎么了退款方法呀？是能退回来是。",
                    "speaker": "staff"
                },
                {
                    "content": "什么这是什么多少钱呢？😡",
                    "speaker": "customer"
                },
                {
                    "content": "您这边如果说已经提交了退费申请，我们的系统会根据您所提供的账号信息帮您去进行一个核实和确认。您这边的话只需要您现在只需要留意我们小程序给到您的一个推送通知就可以了。您以上面的一个推送消息为准。",
                    "speaker": "staff"
                },
                {
                    "content": "哦，那行，那你们尽量就帮我去就是。",
                    "speaker": "customer"
                },
                {
                    "content": "就是退全款吗。😡",
                    "speaker": "customer"
                },
                {
                    "content": "您这个申请退款能给您退回多少，我没有办法给到您准确答复的。先生，您要以您的一个实际退费的情况为准的，好吗？",
                    "speaker": "staff"
                },
                {
                    "content": "哦，他也没有一个期限是吗？😮",
                    "speaker": "customer"
                },
                {
                    "content": "这个我们系统会帮您去进行核实的，您不用担心，建议您这边的话，现在可以留意我们小程序给到您的一个推送通知。",
                    "speaker": "staff"
                },
                {
                    "content": "啊，他他不是说那个他不一定的，他是他就你们那边退款，他是没有一个期限的。就比如说半年之内的钱退回还是多少，他是他是怎么回事，他是审核完审通过审核以后，做是确定就是怎么个还怎就是还给我们多少，是这么回事吗？😡",
                    "speaker": "customer"
                },
                {
                    "content": "是的。",
                    "speaker": "staff"
                },
                {
                    "content": "哦，我还以为我我看都说是就是半年，还有就是说90天的，不是这么一回事，是吗？",
                    "speaker": "customer"
                },
                {
                    "content": "并没有这种说法，先生，请您不要相信其他平台的所传信息。哦，那行，那好的，我知道了。那他大概是什么时候能给我一个答复我，我这前几天就已经申请了。",
                    "speaker": "customer"
                },
                {
                    "content": "您现在的话只需要留意我们小程序，它上面给到您的一个推送消息就可以了。您提交之后，它都会会把您的这个申请退费的一个过程和以及步骤在我们的小程序上面去给您进行推送的。您留意一下。",
                    "speaker": "staff"
                },
                {
                    "content": "啊，那行，那好的。😊",
                    "speaker": "customer"
                },
                {
                    "content": "那我如果没有其他问题。",
                    "speaker": "staff"
                }
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
