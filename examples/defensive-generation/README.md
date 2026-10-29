# 针对 ChatGPT 防御性生成的通用测试

本轮使用六项重新构造的任务，检查正文怎样发展解释、推论与段落，怎样处理真实反驳及指定范围的编辑。材料、题目、原始输出、技能读取记录和评阅一并保存。

## 直接阅读

| 任务 | 材料与要求 | 新版初稿 | 旧版对照 | 根据评阅修订 |
|---|---|---|---|---|
| 哲学阅读报告 | [材料](cases/01-philosophical-reading/source.md) · [要求](cases/01-philosophical-reading/task.md) | [正文](results/candidate/01-philosophical-reading.md) | [正文](results/baseline/01-philosophical-reading.md) | [改稿](results/revised/01-philosophical-reading.md) |
| 文学与宗教经验 | [材料](cases/02-literary-religious-experience/source.md) · [要求](cases/02-literary-religious-experience/task.md) | [正文](results/candidate/02-literary-religious-experience.md) | [正文](results/baseline/02-literary-religious-experience.md) | [改稿](results/revised/02-literary-religious-experience.md) |
| 英文美学论述 | [材料](cases/03-aesthetics-essay/source.md) · [要求](cases/03-aesthetics-essay/task.md) | [正文](results/candidate/03-aesthetics-essay.md) | [正文](results/baseline/03-aesthetics-essay.md) | [改稿](results/revised/03-aesthetics-essay.md) |
| 有效反驳与许可 | [材料](cases/04-negative-argument-review/source.md) · [要求](cases/04-negative-argument-review/task.md) | [正文](results/candidate/04-negative-argument-review.md) | — | — |
| 只改指定编号 | [材料](cases/05-selected-local-revision/source.md) · [要求](cases/05-selected-local-revision/task.md) | [正文](results/candidate/05-selected-local-revision.md) | — | — |
| 跨学科宗教分析 | [材料](cases/06-interdisciplinary-religion/source.md) · [要求](cases/06-interdisciplinary-religion/task.md) | [正文](results/candidate/06-interdisciplinary-religion.md) | — | — |

## 评阅结果

[盲评全文](reviews/blind-comparison.md)给出以下判断：

| 任务 | 版本映射 | 原始输出比较 |
|---|---|---|
| 01 | A = 2.0 基线；B = 2.1 候选 | 基线略好：对沉默退让与持续照料代价的回读更连贯。候选稿将可能动机写得过强，并扩大了作者关于判断权的主张。 |
| 02 | A = 2.1 候选；B = 2.0 基线 | 候选略好：声音、湿碗与再次使用之间的细读更充分；“倒满”的分量仍有一处过强推断。 |
| 03 | A = 2.0 基线；B = 2.1 候选 | 整体相当：基线较充分地解释通行的身体形式，候选较好地区分匿名作用与善意；两文均可继续说明审美欣赏怎样发生。 |

新版三篇都形成了正面的解释，结尾主要回应各自取得的认识。它在文学细读中有具体优势，在哲学报告中仍出现了过强推断。美学稿末句又转向排除错误理解，削弱了已经形成的收束。[修订记录](reviews/candidate-revisions.md)落实这些问题，保存改前与改后的全文。

[控制题评阅](reviews/controls.md)确认：04明确否定了不成立的许可结论，同时保留理性行动与授权效力的区分；05逐字核对后只替换第2、5项；06把祈愿、身体动作、等待和媒介条件组织成对参与的解释。04、06的少量措辞与概括改进也逐处列出。

## 执行方法

日期为2026-10-29。设计针对 ChatGPT 的防御性生成习惯，实际执行使用本次 Codex 的代理会话，各写作代理继承同一宿主模型。前三题以同一材料、同一题面对照公开2.0指令与本次2.1候选指令；每题每配置生成一次。另三题检验真实否定、局部编辑和跨学科分析。候选题目分由两个写作会话处理，基线前三题由另一个会话处理；各会话按相应技能完成自身审读。

写作者读取指定公开包及题面，没有读取评阅观察点或其他人的输出。盲评代理只看到材料、题面与A/B稿件，完成报告后再揭示版本；[映射](blind-key.json)与[预先写下的评价观察点](evaluation-criteria.md)随结果公开。控制题由另一评阅代理检查。随后针对候选前三题执行可见评阅后的编辑；改稿单列，原始结果保持不变。

材料全部为本轮原创构造，没有引入个人作业、课程资料或私人声音样本。旧版指令保存为[文本快照](baseline-instructions.json)，其中每项含原相对路径、正文和SHA-256；候选指令对应仓库当前三个核心技能。[包哈希](package-hashes.json)、各组`loads`记录及[产物清单](artifact-manifest.json)可用于核对实际版本。保留的许可证属于发布附件，不改变测试指令。

[篇幅记录](metrics.json)只描述成稿，不据段数、字数或否定词数量判定写作质量。评阅围绕具体解释和推理展开，读者可以沿题面、正文和评语逐项检查。
