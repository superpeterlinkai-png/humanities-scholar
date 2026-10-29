# 既有通用案例的审读与修订

本组记录展示候选技能怎样处理已有文字：先读原始任务和旧稿，定位实际问题，再完成修订与回读。执行日期为 2026-10-29，使用 `humanities-review` 与 `humanities-writing` 入口。这是可见旧稿后的定向编辑记录。

| 案例 | 材料 | 旧稿的有效部分 | 本次改进 |
| --- | --- | --- | --- |
| [Mill 研究问题](01-mill-research-question/source/input.md) | 《论自由》第二章四个公版节选 | 对真假与理解的区分、E4 的替代问题、可执行的阅读计划 | 解释教师转述、真实论敌和想象反驳的关系；删除与题目无关的预防性否定。 |
| [作品同一性与翻译](02-argument-and-translation/source/input.md) | 原创构造段落及分阶段修订要求 | 对 S3、S5 推论的诊断，以及译文对否定、可能性的保留 | 在同一个例子中解释感受与解释主张的转换，完成中文段落并同步英文。 |
| [仪式安静](retained-validation/01-ritual-silence/review.md) | 虚构规约、申辩与更正后的讽喻故事 | 材料文类更正与规范、行为的区分 | 展开“帮助听见”怎样改变对低语的判断，接续已经更正的材料。 |
| [音乐作品及后续论证](retained-validation/02-musical-work/review.md) | 构造的作品同一性备忘录、两句英译；无误预判与自由的后续任务 | 对隐含前提和模态范围的辨析 | 把辨析推进为有具体理由的论述，分别处理完整正文与限定英译。 |
| [文学细读](retained-validation/03-literary-waiting/review.md) | 原创开灯短篇与独立方法附注 | 对“没有等”与叙事次序的分析 | 连贯展开否认怎样参与叙述，保留题目指定的方法判断。 |

每例的 `source/input.md`、`source/prompts.md` 与 `old-output.md` 是来源快照；`review.md` 记录旧稿位置、判断、修法和对实际改稿的回读；`revision.md` 为本次改稿。源文件与校验值见 [source-manifest.json](source-manifest.json)，实际读取的技能文件及版本哈希见 [skill-read-manifest.json](skill-read-manifest.json)。

来源仓库为 `humanities-skills-suite`，提交为 `437ea2c07d4563ed50accf6ee97532b21e2129c0`；具体来源使用仓库相对路径记录。原材料的编辑性质与来源说明保存在输入和旧稿中。[NOTICE.md](NOTICE.md) 说明署名、许可及修改。

后三组来自本仓库较早的 `validation/`，原稿和输入继续保留；相邻的 `review.md` 与 `revision.md` 展示本次变化。各例的 `source/` 保存任务与旧输出快照，[对应清单](retained-source-manifest.json)核对它们与原文件的字节一致性；`loads.json` 记录实际读取的候选技能及哈希。音乐例的后续独立任务另见 [transfer-revision.md](retained-validation/02-musical-work/transfer-revision.md)。

## 阅读结果

密尔示例的表格与小标题服务于选题备忘录，保留了这些形式。改稿把原来两段相容的“解释／反读”推进为对 E4 两组要求的比较，并形成关于论证工作的判断。

作品同一性示例的否定承担了所选结论，改稿保留这些否定。新增分析说明：感受的不同可以为解释带来不同任务，而解释的理由仍可比较。英译以修订后的中文为准。

技能使用记录仅列本轮实际读取的文件。检查覆盖源文件快照一致性、原稿定位、论证变化及中英对应；执行记录见 [verification.json](verification.json)。
