# 2.0.0 · 2026-10-13

- 以研究、写作、审读作为三个主要入口，内部按需调用问题设计、来源、细读、概念、论证、作者声音等专项。每个入口包含完整依赖；七项可选专项另行保留。
- 长稿续写接续已取得的认识；审读实际重建支持链并比较远隔重复段落；表达检查保留有内容的否定，删除空泛自我保证。
- 保留限定编辑范围、先列编号、只改选中项和替换后上下文检查；公开版提供偏好采集方法，不预填私人档案。
- 公开六个主题的十四篇长文、八份配对评审与段落定位。初次比较并未全面偏好整合版；两项优化后复测有小幅改善，仍保留失败记录。
- 更新安装器和结构校验以支持当前十项目录，加入案例计数、哈希、定位及私人路径检查。首次安装拒绝覆盖已有目录。
- 旧版本的独立入口需在备份后迁出活动技能目录，避免与整合入口重复触发。

---

# 1.1.0：六项真实研究之后的局部改进

2026-09-22。本次改动以六领域完整文章研究中的实际摩擦为依据；原始1.0.0压缩包保留。未更名技能、改变自动发现设置、增加审批步骤或把研究改成固定流水线。

| 文件 | 改变的判断动作 | 实际依据 |
|---|---|---|
| [humanities-close-reading](https://github.com/superpeterlinkai-png/humanities-scholar/blob/v1.1.0/skills/humanities-close-reading/SKILL.md) | 借原文或注释支持解释时，同时处理相邻不利限定 | 《解蔽》初稿选择性借杨注支持开放解释 |
| [humanities-argument](https://github.com/superpeterlinkai-png/humanities-scholar/blob/v1.1.0/skills/humanities-argument/SKILL.md) | 保留对手的弱要求与适用条件；区分构造靶子和真实学者；防止解释垄断反例相关性 | 中国哲学的弱对照、美学的反思强度与封闭解释、元伦理学的比较论域 |
| [humanities-scholarship](https://github.com/superpeterlinkai-png/humanities-scholar/blob/v1.1.0/skills/humanities-scholarship/SKILL.md) | 与最近的已读论证比较具体增量；新发现覆盖贡献时同步改引言摘要 | 白奚、Barnett、Sliwa等近邻研究实际改变选题与贡献；这是强化已有有效行为 |
| [批判性方法](https://github.com/superpeterlinkai-png/humanities-scholar/blob/v1.1.0/skills/humanities-research/references/methods/critical-genealogical.md) | 检查制度承诺覆盖者与要求保护者是否同一范围；扩展需额外理由 | 后现代稿把内在承诺推向所有受影响者 |
| [历史与语文学](https://github.com/superpeterlinkai-png/humanities-scholar/blob/v1.1.0/skills/humanities-research/references/methods/historical-philological.md) | 论点取决于字形、标点或异文时，区分实际见证及整理层 | 《荀子》电子文本与后世注疏不能直接证明原作者的字形意图 |
| [humanities-source-discovery](https://github.com/superpeterlinkai-png/humanities-scholar/blob/v1.1.0/skills/humanities-source-discovery/SKILL.md) | 冲突元数据回查实际文件；区分转录、抽取与原页核实；识别挑战页及空抽取 | 同名德里达版本、英伽登转录、错误网页栏目和抓取日期 |
| [写作交付](https://github.com/superpeterlinkai-png/humanities-scholar/blob/v1.1.0/skills/humanities-writing/references/genres-and-delivery.md) | 有明确长度约束时按约定范围复算正文 | 正文字数与含标题、书目的总字符数不同 |

不是每项修改都来自基线缺陷。有些问题主要是未执行已有原则，有些新增提示只是让已有成功更易复用。来源网站403或扫描件不能提取，不被计作学术方法失败。

宗教哲学中的规范桥接归属、分析哲学中的模型适用范围，主要通过已有细读、论证及审读能力修复，没有再为每个个例增加一条规则。现有模态与支持链要求已经涵盖充分/必要区分；本版没有重复堆叠同义提醒。

精确改动见 [文件差异](validation/candidate.diff)，验证及其限制见 [验证报告](VALIDATION.md)。此次行为结果不能证明这些提示在一切新课题中都有效，更不能证明技能本身已经获得博士水平的领域知识。

## 公开适配

本公开包与本地1.1.0在两个声音相关技能文件上不同：移除原使用者的初始偏好，改为每位作者自行形成档案的采集说明。其他33个技能文件保持一致。发布说明与验证记录中的私人路径已清理；原安装未改变。此适配不是新一轮学术能力改进。
