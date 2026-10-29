---
name: voice-dna
description: "Match the user’s voice in everyday emails, posts, notes and nonacademic essays using actual samples and corrections. Academic prose uses humanities-writing. Do not infer fixed beliefs or fabricate experiences to match a voice."
---

# VoiceDNA

This entry focuses on everyday and nonacademic prose. For academic work use humanities-writing. A user explicitly naming VoiceDNA may still use its relevant sample-based guidance; retain the current task’s edit boundary.

Revise drafts toward the user's actual voice, not toward generic "good writing." Ground strong rewrites in real samples, preserve texture and intent, and use anti-slop rules as guidance rather than as a rigid style constitution.

## Workflow

### 1. Frame the job first

- Identify the source draft, intended audience, and purpose.
- Identify the requested edit depth: review only, selected lexical/syntactic changes, light cleanup, moderate rewrite, or strong recast. Review-only requests receive stable numbered proposals; selected-item requests change only the approved items. Do not turn narrow cleanup into general proofreading.
- Default to revision, not ghostwriting from scratch, unless the user clearly asks for a fresh draft.

### 2. Check for real voice evidence

- Start with [references/voice-samples.md](references/voice-samples.md) when that file exists.
- Look for 2-3 real writing samples from the user before doing substantial voice imitation.
- Give explicit user corrections priority. Label samples by provenance: user-authored original, user-authored revision, translation, quotation, or AI-assisted accepted draft. Acceptance is preference evidence, not proof of unaided authorship. Use task and genre boundaries when generalizing.
- If no samples are available and the user wants a strong voice match, ask for samples before rewriting heavily.
- If the user does not provide samples, say confidence is limited and fall back to a light anti-slop edit rather than pretending to know their voice.

### 3. Build a temporary voice profile

- Read [references/voice-profile-template.md](references/voice-profile-template.md) and infer the user's:
  - cadence and paragraph rhythm
  - bluntness vs softness
  - humor or dryness
  - tolerance for fragments and rough edges
  - specificity style and favored details
  - recurring transitions or sentence patterns
  - phrases, tones, or moves that feel fake in their voice
- Let the samples outrank generic writing rules whenever they conflict.

### 4. Rewrite toward the profile

- Preserve the draft's meaning, intent, and emotional temperature.
- Keep the user's edges when they feel deliberate: slight roughness, sharp turns, fragments, dry understatement, or clipped endings.
- Remove obvious sludge: padded transitions, vague abstraction, fake certainty, motivational filler, and stock AI phrasing.
- Prefer sanding off the synthetic layer over recasting the whole piece.
- When in doubt, choose the smaller rewrite that still improves the text.

### 5. Use anti-slop rules as a bias, not a cage

- Read [references/anti-slop-rules.md](references/anti-slop-rules.md) when you need sharper guardrails against generic AI prose.
- Treat recurring phrases as contextual clues, not hard bans. Preserve substantive negation, uncertainty, technical terms, and stable concept names; an entailment denial cannot be replaced by a positive statement about only one side.
- Treat stylistic preferences such as contractions, parentheticals, or em dash avoidance as defaults that can be overridden by the user's samples or the specific piece.
- Never force the output to satisfy a rule that makes it less like the user.

### 6. Return the work cleanly

- Return the requested artifact: findings only for review, revised copy for editing. Check each replacement with neighboring sentences for referents, subjects, transitions, leftover clauses, and citation attribution; protect unchanged selections and locked spans.
- Add a brief note only when useful, for example:
  - what voice signals were preserved
  - what sludge was stripped out
  - whether confidence is limited because samples were missing or thin
- Do not pad the response with a long explanation unless the user asks.

## Defaults

- Prefer short paragraphs and concrete wording when that aligns with the samples.
- Prefer natural contractions unless the user's voice or the moment wants formality.
- Prefer specific nouns and active verbs over inflated abstraction.
- Prefer natural transitions over mechanical connectors.
- Avoid over-explaining the edit.

## Confidence Rules

- High confidence: multiple strong writing samples with consistent traits.
- Medium confidence: one or two decent samples plus a draft with clear signals.
- Low confidence: no real samples, contradictory samples, or only abstract style instructions.
- When confidence is low, say so plainly and keep the rewrite conservative.

## Example Triggers

- "Rewrite this in my voice."
- "Make this sound more like me."
- "De-slop this."
- "Tighten this without making it sound AI-generated."
- "Edit this email but keep my voice."
- "This sounds polished in a bad way. Strip out the generic parts."

## References

- Use [references/voice-profile-template.md](references/voice-profile-template.md) to extract a temporary voice profile from user samples.
- Use [references/voice-samples.md](references/voice-samples.md) as preloaded evidence of the user's voice when it is available.
- Use [references/anti-slop-rules.md](references/anti-slop-rules.md) to catch synthetic phrasing and generic cleanup habits.
