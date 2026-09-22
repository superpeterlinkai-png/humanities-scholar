# Humanities Scholar · 人文学术研究 Skills

面向哲学、宗教学、文学、美学及交叉研究的十项 Codex skills。根据当前研究困难选择下一项工作，推进选题、材料读取、解释、论证、成稿与修订。**版本：1.1.0，公开分发版。**

Ten skills for source-grounded humanities research, argument development, writing, and revision. Chinese instructions support Chinese and English academic work. These skills guide research decisions; they do not supply an expert knowledge database or guarantee doctoral-level results.

## 使用

完整研究任务调用 `$humanities-research`，由其按需读取其他能力。已有材料可直接进入写作，出现解释困难时再返回细读或检索。

> 用 $humanities-research 完成这篇论文。读取已有要求与材料，自主形成并检验暂定论点，补足必要检索和细读，完成正文与审读。保留我已说明的表达偏好，交代实质思想取舍及证据限制。

| Skill | 工作 |
|---|---|
| humanities-research | 全流程推进、研究困难诊断与连续项目衔接 |
| humanities-question-design | 从材料和问题形成研究设计 |
| humanities-source-discovery | 检索原文、确认版本与引用依据 |
| humanities-close-reading | 具体措辞、形式、语境和竞争解释 |
| humanities-scholarship | 重建学者思想、争论与研究介入 |
| humanities-concept-work | 概念分析、理论试用与重构 |
| humanities-argument | 支持链、反例、反驳与主张修订 |
| humanities-author-voice | 依据当前作者样本与偏好适配声音 |
| humanities-writing | 中英文正文、计划、摘要、翻译与编辑 |
| humanities-review | 实质审读、修订及评审回应 |

方法分支包括哲学论证、历史与语文学、现象学与诠释学、批判性研究、宗教实践、文学、美学、比较与翻译。按主张所需的证据选择方法，同一项目可结合多个分支。

## 安装

下载 Releases 中的完整包并解压，需要 Python 3.10 或更高版本，无第三方 Python 依赖。十个技能共享相对路径，须一起安装。

```powershell
python validate.py
python install.py --destination "$env:USERPROFILE\.codex\skills"
```

macOS / Linux 示例：

```sh
python3 validate.py
python3 install.py --destination "$HOME/.codex/skills"
```

`--destination` 应指向当前安装实际使用的技能目录。安装器核对文件哈希、拒绝覆盖已有同名目录，并在写入后回读核验。它是首次安装器；已有安装应先保留个人改动，再明确处理目录冲突。技能是否已被当前会话发现，以实际运行结果为准。

## 设计与验证

本套另建十个入口，并延续此前人文改造工作中的若干原则；不宣称已经彻底重建全部研究机制。六领域完整文章研究后，1.1.0局部修改七个文件，处理选择性引注、弱化对手、贡献定位、规范范围及来源载体等问题。三次非作者模型复测仍发现初审遗漏，已据原文修订。

见 [验证报告](VALIDATION.md)、[改动记录](CHANGES.md)、[设计依据](skills/humanities-research/references/design-sources.md) 和 [来源说明](NOTICE.md)。研究工作与技能效果没有无技能或旧版对照，不能据此认证普遍博士水平、全球原创性或真实作者声音。原始研究稿及私人项目资料不包含在此技能仓库。

公开版仅将个人偏好改为通用采集说明，并清理验证记录中的本机路径；其余33个技能文件与本地1.1.0一致。历史验证哈希对应当时的本地版本；当前公开文件以根目录 `MANIFEST.json` 为准。个人声音需要由每位作者自己的原始文本与纠正建立。

## 校验与维护

```sh
python validate.py
python tests/test_install.py
```

GitHub Actions 对主分支推送和拉取请求运行以上检查。它们验证安装和结构，不替代学术评价。问题报告请避免附带私人文章、个人路径或凭据。

本仓库采用 CC BY-NC-SA 4.0，来源及修改说明见 [NOTICE.md](NOTICE.md)，许可见 [LICENSE](LICENSE)。
