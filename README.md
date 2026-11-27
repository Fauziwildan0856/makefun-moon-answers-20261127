# The Moon Finally Answers Back

[![make.fun](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/c/u-mang-the-moon-finally-answers-back-781a7ec1)
[![Rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/Fauziwildan0856/makefun-moon-answers-20261127/rank.svg)](https://make.fun/c/u-mang-the-moon-finally-answers-back-781a7ec1)
[![Reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/Fauziwildan0856/makefun-moon-answers-20261127/reward.svg)](https://make.fun/c/u-mang-the-moon-finally-answers-back-781a7ec1)

Entry for the [make.fun bounty "The Moon Finally Answers Back"](https://make.fun/c/u-mang-the-moon-finally-answers-back-781a7ec1): one line, 1–240 characters, in the voice of the Moon replying at last to the wishes, howls and late-night promises of everyone staring up at it.

## The entry

> I've heard every wish, every howl, every 3 a.m. 'I swear I'll change.' Four billion years of listening — and you still think I'm the one who owes you a favour.

## How it works

`main.py` (Python standard library only) writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, then reads it back and refuses to exit 0 unless the file holds exactly that 1–240 character text.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
