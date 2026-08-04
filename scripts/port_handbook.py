#!/usr/bin/env python3
"""Port outlabsAuth docs-library Markdown into Nuxt Content (template conventions).

Follows Nuxt UI docs template patterns:
- frontmatter: title, description, navigation.icon
- no H1 in body (UPageHeader owns the title)
- ::tip / ::note / ::warning / ::caution instead of ad-hoc callouts
- root-relative internal links
- code fences prefer ```lang [filename]

Re-run after handbook edits:
  python3 scripts/port_handbook.py
  python3 scripts/port_handbook.py --source ../outlabsAuth-cli --only 10-Command-Line.md

`--source` accepts an outlabsAuth checkout (or its docs-library directory).
`OUTLABS_AUTH_SOURCE` provides the same override for package scripts and CI.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = REPO_ROOT.parent / "outlabsAuth"
DST = REPO_ROOT / "content"

# SKIP hand-crafted Nuxt-style pages
SKIP = {
    "00-Introduction.md",
    "01-Getting-Started.md",
    "02-Routers-and-Prefixes.md",
    "03-Configuration.md",
    "07-Choosing-a-Preset.md",
    "08-Deployment.md",
}

PAGES: list[tuple[str, str, str, str, str]] = [
    ("02-Routers-and-Prefixes.md", "2.build/1.routers-and-prefixes.md", "Routers & Prefixes", "Which get_*_router factories to mount and how prefixes work.", "i-lucide-route"),
    ("03-Configuration.md", "2.build/2.configuration.md", "Configuration", "Secrets, schema, Redis, cache backends, and CLI.", "i-lucide-settings"),
    ("09-Background-Maintenance.md", "1.getting-started/5.background-maintenance.md", "Background Maintenance", "Run cleanup and sync work safely outside FastAPI processes.", "i-lucide-timer-reset"),
    ("10-Command-Line.md", "2.build/4.cli.md", "Command Line", "Operate OutlabsAuth without a UI, from a terminal or coding agent.", "i-lucide-terminal"),
    ("04-OAuth-and-Social-Login.md", "3.auth/1.oauth-and-social-login.md", "OAuth & Social Login", "Provider routers, invite-only login, link and unlink.", "i-lucide-log-in"),
    ("05-Sessions-and-Audit.md", "3.auth/2.sessions-and-audit.md", "Sessions & Audit", "Active sessions and user audit search.", "i-lucide-monitor-smartphone"),
    ("06-Passwordless-and-Messaging.md", "3.auth/3.passwordless-and-messaging.md", "Passwordless & Messaging", "Magic links, access codes, and host-owned delivery.", "i-lucide-mail"),
    ("22-JWT-Tokens.md", "3.auth/4.jwt-tokens.md", "JWT Tokens", "Access and refresh token behavior.", "i-lucide-key-round"),
    ("23-User-Management-API.md", "3.auth/5.user-management-api.md", "User Management API", "Admin and self-service user HTTP surface.", "i-lucide-users"),
    ("24-User-Invitations.md", "3.auth/6.user-invitations.md", "User Invitations", "Invite-by-email onboarding.", "i-lucide-send"),
    ("25-Roles-and-Permissions.md", "3.auth/7.roles-and-permissions.md", "Roles & Permissions", "Permission catalog and role definitions.", "i-lucide-shield"),
    ("26-ABAC.md", "3.auth/8.abac.md", "ABAC", "Attribute conditions on roles and permissions.", "i-lucide-filter"),
    ("48-User-Status-System.md", "3.auth/9.user-status.md", "User Status", "Active, invited, suspended, banned, deleted.", "i-lucide-user-cog"),
    ("13-Core-Authorization-Concepts.md", "4.enterprise/1.core-authorization-concepts.md", "Core Authorization Concepts", "Users, roles, permissions, entities, and tree access.", "i-lucide-network"),
    ("51-Entities.md", "4.enterprise/2.entities.md", "Entities", "Enterprise org tree CRUD, move, children, path.", "i-lucide-folder-tree"),
    ("54-Entity-Memberships.md", "4.enterprise/3.entity-memberships.md", "Entity Memberships", "Enterprise membership lifecycle.", "i-lucide-user-plus"),
    ("50-API-Key-Host-Integration.md", "5.integrations/1.api-keys.md", "API Keys", "Personal and system integration keys for host apps.", "i-lucide-key"),
    ("12-Data-Models.md", "6.reference/1.data-models.md", "Data Models", "Postgres / SQLModel schema reference.", "i-lucide-database"),
    ("49-Activity-Tracking.md", "6.reference/2.activity-tracking.md", "Activity Tracking", "DAU / MAU style engagement counters.", "i-lucide-activity"),
    ("95-Testing-Guide.md", "6.reference/3.testing.md", "Testing", "Run and extend library and host tests.", "i-lucide-flask-conical"),
    ("97-Observability.md", "6.reference/4.observability.md", "Observability", "Metrics and logs without taking over your FastAPI app.", "i-lucide-eye"),
    ("98-Metrics-Reference.md", "6.reference/5.metrics-reference.md", "Metrics Reference", "Prometheus metric catalog.", "i-lucide-chart-bar"),
    ("99-Log-Events-Reference.md", "6.reference/6.log-events-reference.md", "Log Events Reference", "Structured log event catalog.", "i-lucide-scroll-text"),
]

NAV = {
    "1.getting-started": ("Getting Started", "i-lucide-rocket"),
    "2.build": ("Build", "i-lucide-wrench"),
    "3.auth": ("Auth", "i-lucide-lock"),
    "4.enterprise": ("Enterprise", "i-lucide-building-2"),
    "5.integrations": ("Integrations", "i-lucide-plug"),
    "6.reference": ("Reference", "i-lucide-book-marked"),
}

LINK_MAP: dict[str, str] = {}
for src, dest, *_ in PAGES:
    path = "/" + "/".join(
        part.split(".", 1)[-1] if re.match(r"^\d+\.", part) else part
        for part in Path(dest).with_suffix("").parts
    )
    LINK_MAP[src] = path
    LINK_MAP[src.replace(".md", "")] = path
    LINK_MAP[re.sub(r"^\d+-", "", src)] = path

# Hand-crafted routes
LINK_MAP.update({
    "00-Introduction.md": "/getting-started/introduction",
    "01-Getting-Started.md": "/getting-started/getting-started",
    "07-Choosing-a-Preset.md": "/getting-started/choosing-a-preset",
    "08-Deployment.md": "/getting-started/deployment",
    "Introduction.md": "/getting-started/introduction",
    "Getting-Started.md": "/getting-started/getting-started",
    "Choosing-a-Preset.md": "/getting-started/choosing-a-preset",
    "Deployment.md": "/getting-started/deployment",
})

ALIASES = {
    "README.md": "/getting-started/introduction",
    "./README.md": "/getting-started/introduction",
    "../docs/AUTH_UI.md": "/integrations/outlabsauth-ui",
    "../docs/COMPARISON_MATRIX.md": "/getting-started/choosing-a-preset",
    "../docs/API_DESIGN.md": "https://github.com/outlabsio/outlabsAuth/blob/main/docs/API_DESIGN.md",
    "../docs/DEPLOYMENT_GUIDE.md": "/getting-started/deployment",
    "../docs/AUTH_EXTENSIONS.md": "/auth/passwordless-and-messaging",
    "../docs/SECURITY.md": "/getting-started/deployment",
    "../docs/DESIGN_DECISIONS.md": "https://github.com/outlabsio/outlabsAuth/blob/main/docs/DESIGN_DECISIONS.md",
    "../docs/TESTING_GUIDE.md": "/reference/testing",
    "../docs/LIBRARY_ARCHITECTURE.md": "/enterprise/core-authorization-concepts",
    "../docs/API_KEY_SCOPE_AND_GRANT_POLICY_EPIC.md": "/integrations/api-keys",
    "../docs/CLI_DESIGN.md": "https://github.com/outlabsio/outlabsAuth/blob/main/docs/CLI_DESIGN.md",
    "../docs/CLI_AGENT_GUIDE.md": "https://github.com/outlabsio/outlabsAuth/blob/main/docs/CLI_AGENT_GUIDE.md",
    "../docs/CLI_MANIFEST.md": "https://github.com/outlabsio/outlabsAuth/blob/main/docs/CLI_MANIFEST.md",
    "../docs/WHATSAPP_ACCOUNT_MESSAGING.md": "/auth/passwordless-and-messaging",
    "../docs/PRIVATE_RELEASE.md": "/reference/testing",
    "../examples/": "https://github.com/outlabsio/outlabsAuth/tree/main/examples",
    "../examples": "https://github.com/outlabsio/outlabsAuth/tree/main/examples",
    "../observability/": "https://github.com/outlabsio/outlabsAuth/tree/main/observability",
    "../tests/README.md": "https://github.com/outlabsio/outlabsAuth/blob/main/tests/README.md",
}
LINK_MAP.update(ALIASES)


def strip_h1(body: str) -> str:
    lines = body.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        if lines and lines[0].strip() == "":
            lines = lines[1:]
    return "\n".join(lines)


def banner_to_note(body: str) -> str:
    lines = body.splitlines()
    banner: list[str] = []
    i = 0
    while i < len(lines) and (lines[i].startswith("> ") or lines[i].strip() == ">"):
        banner.append(re.sub(r"^>\s?", "", lines[i]))
        i += 1
    if not banner:
        return body
    rest = "\n".join(lines[i:]).lstrip("\n")
    text = " ".join(b.strip() for b in banner if b.strip())
    text = re.sub(r"Part of the \[OutlabsAuth Handbook\]\([^)]+\)\.?\s*", "", text)
    text = re.sub(r"\*\*Handbook[^*]*\*\*\s*[·•-]?\s*", "", text).strip()
    text = re.sub(r"Related:.*$", "", text).strip()
    if not text:
        return rest
    # Prefer ::note for audience banners
    return f"::note\n{text}\n::\n\n{rest}"


def normalize_callouts(body: str) -> str:
    # Convert our earlier ::callout{icon=...} to ::tip / ::note
    body = re.sub(
        r"::callout\{icon=\"i-lucide-info\"\}\n([\s\S]*?)::",
        r"::note\n\1::",
        body,
    )
    body = re.sub(
        r"::callout\{[^}]*\}\n([\s\S]*?)::",
        r"::tip\n\1::",
        body,
    )
    # Honest caveat / do not → warning
    body = re.sub(
        r"> \*\*Honest caveat:\*\* ([^\n]+)",
        r"::warning\n\1\n::",
        body,
    )
    body = re.sub(
        r"> \*\*Caveat:\*\* ([^\n]+)",
        r"::warning\n\1\n::",
        body,
    )
    return body


def rewrite_links(body: str) -> str:
    def repl(m: re.Match[str]) -> str:
        label, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        bare = url.split("#")[0]
        frag = "#" + url.split("#", 1)[1] if "#" in url else ""
        for key in (bare, bare.lstrip("./"), Path(bare).name):
            if key in LINK_MAP:
                return f"[{label}]({LINK_MAP[key]}{frag})"
        if "examples/" in bare:
            rel = bare.replace("../", "")
            return f"[{label}](https://github.com/outlabsio/outlabsAuth/tree/main/{rel})"
        if bare.startswith("../"):
            return f"[{label}](https://github.com/outlabsio/outlabsAuth/tree/main/{bare[3:]})"
        return m.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, body)


def tidy_code_fences(body: str) -> str:
    # ```python without filename stays; add common filenames for bash
    body = re.sub(r"^```bash\n", "```bash [Terminal]\n", body, flags=re.M)
    body = re.sub(r"^```sh\n", "```bash [Terminal]\n", body, flags=re.M)
    return body


def write_page(source: Path, src_name: str, dest_rel: str, title: str, description: str, icon: str) -> None:
    if src_name in SKIP:
        print(f"skip (hand-crafted) {src_name}")
        return
    src = source / src_name
    text = src.read_text()
    body = strip_h1(text)
    body = banner_to_note(body)
    body = normalize_callouts(body)
    body = rewrite_links(body)
    body = tidy_code_fences(body)
    # Drop stale “handbook later / Nuxt later” asides
    body = re.sub(
        r"> This handbook is Markdown[\s\S]*?first\.\n?",
        "",
        body,
    )
    out = DST / dest_rel
    out.parent.mkdir(parents=True, exist_ok=True)
    fm = (
        f"---\n"
        f"title: {title}\n"
        f"description: {description}\n"
        f"navigation:\n"
        f"  icon: {icon}\n"
        f"---\n\n"
    )
    out.write_text(fm + body.rstrip() + "\n")
    print(f"wrote {out.relative_to(DST)}")


def write_nav() -> None:
    for folder, (title, icon) in NAV.items():
        path = DST / folder / ".navigation.yml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"title: {title}\nicon: {icon}\n")


def write_ui_page() -> None:
    # Hand-crafted Nuxt Content page — do not overwrite on port.
    dest = DST / "5.integrations/2.outlabsauth-ui.md"
    if dest.exists():
        print(f"skip (hand-crafted) {dest.relative_to(DST)}")
        return
    raise SystemExit(
        f"missing hand-crafted UI page: {dest} — restore content/5.integrations/2.outlabsauth-ui.md"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Port the outlabsAuth implementer handbook into Nuxt Content."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(os.environ.get("OUTLABS_AUTH_SOURCE", DEFAULT_SOURCE)),
        help="outlabsAuth checkout or docs-library directory (default: sibling outlabsAuth)",
    )
    parser.add_argument(
        "--only",
        action="append",
        choices=[page[0] for page in PAGES],
        metavar="SOURCE_FILE",
        help="port only this handbook page; repeat for more than one page",
    )
    return parser.parse_args()


def resolve_source(source: Path) -> Path:
    source = source.expanduser().resolve()
    handbook = source if source.name == "docs-library" else source / "docs-library"
    if not handbook.is_dir():
        raise SystemExit(
            f"handbook source not found: {handbook} "
            "(pass --source or set OUTLABS_AUTH_SOURCE)"
        )
    return handbook


def main() -> None:
    args = parse_args()
    source = resolve_source(args.source)
    print(f"source {source}")
    write_nav()
    selected = PAGES
    if args.only:
        requested = set(args.only)
        selected = [item for item in PAGES if item[0] in requested]
    for item in selected:
        write_page(source, *item)
    write_ui_page()
    print("done")


if __name__ == "__main__":
    main()
