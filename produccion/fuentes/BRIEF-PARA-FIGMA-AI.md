# Salverna — Figma AI design brief
Status: exploratory design proposal, not approved artwork or production game code. Updated 2026-10-13. This brief supersedes the obsolete weekly-exclusion rule and old skills in the historical v1 specification.

## Product and audience
Design a portrait Android social-season game for adult players who enjoy character-driven romance, social manoeuvring and accessible planning. The player is a matchmaker arranging invitations for eight adults. The world is Salverna, a fictional aristocratic mercantile monarchy with subtle supernatural identities. The city is Valcenda. Use Bridgerton as a reference for social theatre and elegant occasion-specific dress, not copied characters or heraldry. Dispatch informs assignment, complementary skills and event interruptions. Candy Crush screenshots inform mobile hierarchy, readable map markers and elevated playful map perspective, not candy colours, level ladders or commercial mechanics.

## Deliverable distinction
For Figma Make: create a client-side interactive web prototype of the future Android game, not an Android APK or Godot project. For Figma Design/First Draft: create editable native design frames and components, not a single flattened screenshot. Do not claim one output automatically supplies the other.

## First scope: six connected screens only
1. Weekly city map in planning mode.
2. Event details.
3. Full invitation letter.
4. Guest assignment with horizontal portrait roster and comparative radar.
5. Guest profile, presented as a full view or accessible overlay.
6. Weekly calendar with reservations and reply confirmation.

Do not add the title sequence, queen's audience, desk, memory game, shop, monetisation or all season outcomes in the first generation. Keep their future existence in mind without placing unused buttons. Start the preview on the city map.

## Non-negotiable game rules
- Plan and reply to invitations for the entire upcoming week BEFORE execution starts. Dates are shown during planning.
- After replies are confirmed, the week executes chronologically on the city map. Do not require the player to plan each day again.
- Events may last multiple days including travel. Participants remain reserved from departure through return; for this test use inclusive whole-day intervals and availability on the following day.
- Activities on the same date can occur concurrently for different people. A person cannot attend overlapping intervals.
- At event time, an unexpected incident may pause progression and request a choice or replacement. This is separate from ordinary pre-week planning.
- A previously completed event cannot be retroactively reassigned. Future letters remain assigned unless an authored exception requires a replacement.
- Mandatory story commitments and optional invitations are distinct. Story continues through unsuccessful outcomes; never create a deadlock if no substitute exists.
- Five skills: Baile/Dance, Estatus/Standing, Chisme/Gossip, Presencia/Presence, Intelecto/Intellect. Values for the prototype are 0–5. Gossip means social information handling and manoeuvring, not automatic truth detection. Standing is not the player's reputation. Presence does not cause attraction.
- Show a pentagonal radar. Event requirements and selected party capabilities have distinct outlines, translucent fills and explicit labels. Mathematical success formula is undecided; use clearly illustrative values, not an invented authoritative success percentage.
- Closeness, romantic attraction and public reputation are different. Do not expose orientation or secret attraction in profiles. Adult placeholders A–H are fixtures, not final characters.

## Layout and visual direction
Reference frame: 432 × 768 (9:16). Adapt to widths around 360–432 and taller phones without stretching portraits, clipping text or placing controls under system bars. Centre the phone-sized application in a wider desktop preview; do not wrap gameplay in a desktop dashboard.

Persistent top area: current date as primary information, week number and settings secondary. Persistent bottom destinations: Ciudad/City, Elenco/Cast, Calendario/Calendar. One clearly prioritised contextual action. Screens requiring full reading may simplify navigation while preserving an obvious return.

The map occupies most of the screen. Five recognisable venues: ballroom, gardens, academy, theatre and residence; these are provisional labels rather than final geographic lore. Elevated oblique 2D view, coherent building perspective, varied silhouettes and readable paths. Markers and head portraits prioritise readability over geographic scale. Do not turn it into a Candy Crush linear numbered level path.

Art direction: elegant, lively, theatrical and painterly. Cool neutral paper, deep berry action colour, ink/navy text, restrained gold progress accents and natural greens/blues. These are starting constraints, not a requirement to reuse a rigid palette. Avoid global sepia/yellow tint, generic grey dashboards, glossy candy rendering and unnecessary ornamental clutter. If an approved illustration reference is attached, transfer its painting language rather than copying a face or costume. Use intentional illustrated placeholders when final art is absent.

Readable body type, expressive serif headings, cursive only for letter salutation/signature or short accents. Live text, meaningful hierarchy, comfortable contrast, approximately 48 logical-pixel touch targets for the mockup, with actual dp conversion/device testing deferred to implementation. Icon plus label for navigation and unfamiliar actions. Colour is never the sole indication of a state.

Use shared components and tokens for buttons, cards, navigation, portrait states, status badges, progress rings and skill labels. In Figma Design, use Auto Layout for text/content relationships. In Make, build equivalent reusable components. Do not bake text, controls or markers into a background image.

## Six-screen behaviour
MAP: a closed envelope marks an available invitation. Tapping it opens details directly. A venue with multiple invitations opens a short agenda, not stacked overlapping markers.
DETAILS: title, host, two short sentences about the situation, date interval, capacity, key skill requirements, main benefit/risk, selected attendees and a clear assign action. A visible letter thumbnail with Leer invitación/Read invitation opens the full letter.
LETTER: a full-reading view with paper, letterhead, readable body and signature. Returning preserves event context and current selection. Important assignment requirements are not hidden in the letter.
ASSIGNMENT: compact vertical portraits in a horizontally scrollable bottom strip. Tapping assigns to a visible slot; a separate explicit action opens a profile. Swiping never assigns. Selected guests remain visible in slots while scrolling. Occupied portraits show the conflicting event and date. A tap-based method is required; dragging is optional. Confirmation is inactive until capacity and availability are valid, with a reason displayed. The radar changes when guests are selected or removed.
PROFILE: portrait, provisional identity label, five skills, date-based availability, known wishes/confidences and visible temporary conditions. No sexuality label, hidden compatibility percentage or omniscient secrets. Return to the exact previous assignment without losing selection.
CALENDAR: show multi-day spans, departures and returns, assigned guests and pending mandatory invitations. Tap an assignment to edit it before week execution. Do not silently remove existing reservations. Begin week requires explicit confirmation; it will be wired to execution in phase two.

## Test fixture
Week 1 covers days 27–30 of early autumn; labels are fixtures, not a new canonical calendar.
- Riverside outing: days 28–30 inclusive, two guests A+B already assigned.
- Ballroom reception: day 29, two guests to assign C+D.
- Theatre visit: day 30, D+E already assigned. This does not overlap D's day-29 reception.
- Dance class: day 29, one seat. Assigning C or D conflicts with the reception; G/H are available.
- All A–H are adults. Distinguish silhouettes/portrait accents without inventing canonical biographies.

## State and navigation requirements
Keep selections, reservations, current event and language in client-side state across screen changes. Refresh persistence is optional for the initial draft, but clearly report whether it exists. Use a single event list, roster and reservation model rather than duplicated hardcoded data per screen. Back/close never confirms, spends or resets. Do not leave decorative buttons pretending to work; connect them, show them disabled with explanation, or omit them. Settings may initially contain a functioning ES/EN switch only.

All interface copy must support Spanish and natural English. Default Spanish for this review. Use a dictionary with stable keys rather than duplicating unrelated layouts per language. Retain dates and assignments on language change. Sample invitation prose is original placeholder copy, not final lore.

## Phase two: only after first-layout review
Preserve the chosen visual language. Add chronological map execution, concurrent portrait travel, ongoing multi-day activities, incident, replacement, result and weekly close.
- Two portraits follow a prepared path; no body walk cycle is required.
- A yellow ring shows elapsed progress around a venue marker, not an entire irregular building.
- Red ring plus exclamation means attention, including opportunities, not necessarily failure.
- An incident pauses the global simulation until resolved; rings resume from saved progress.
- Completed ring plus report envelope opens the conclusion; acknowledgement removes urgency but preserves history.
- Day 28: A+B leave for gardens. Day 29: they remain away while C+D attend the ballroom. A scripted problem makes D unavailable on day 30. At the theatre event's start, ask for a replacement among available people; do not show D arriving first. F is available, A/B still away. Permit a written withdrawal outcome if no replacement.
- Completion and reading are separate. Rewards apply once even if a report is reopened.
- Calendar progression is scripted and player-paced, not a real-time waiting mechanic. Motion may be accelerated/skipped. Do not use randomness in the preview or invent the final probability formula.

## Acceptance checks
Demonstrate: open invitation; read and return from letter; select C; inspect profile and return with C selected; add D; see team radar change; confirm; see C+D on day 29 calendar; try A and receive the correct 28–30 conflict; demonstrate the class conflict; switch ES/EN without resetting state. No portrait distortions, overlapping fixed bars, clipped body copy or vertically hidden choice buttons.

Explain at most three significant design choices and list limitations. Do not assert usability is verified just because a prototype renders.
