# Safe Desktop Sync (Pull only mind-map work without losing local dissertation edits)

Use this if your desktop repo may contain unpushed local edits and you want to bring in only the new mind-map files safely.

## 1) Inspect local state first

```bash
git status
git branch --show-current
```

If you see local changes, do **one** of these before pulling:

### Option A — commit WIP snapshot (recommended)

```bash
git switch -c backup/local-before-mindmap-sync-$(date +%Y%m%d-%H%M)
git add -A
git commit -m "WIP backup before mind-map sync"
```

### Option B — stash everything (quick)

```bash
git stash push -u -m "backup before mind-map sync"
```


### If your repo is already clean and synced

If `git status` is clean and you are already on the right branch, you can skip the backup branch/stash step and proceed directly to `git fetch origin`.

## 2) Fetch remote without changing working tree

```bash
git fetch origin
```

## 3) Review exactly what will come down

```bash
git diff --name-status HEAD..origin/<your-branch>
```

You should see mainly these new/updated files:

- `scripts/build_argument_graph.py`
- `scripts/run_mindmap.sh`
- `mindmap/index.html`
- `mindmap/app.js`
- `mindmap/styles.css`
- `mindmap/README.md`
- `mindmap/argument_graph.json`
- `docs/mindmap_implementation_plan.md`

## 4) Bring in only specific files (safest selective method)

```bash
git checkout origin/<your-branch> -- scripts/build_argument_graph.py scripts/run_mindmap.sh mindmap/index.html mindmap/app.js mindmap/styles.css mindmap/README.md mindmap/argument_graph.json docs/mindmap_implementation_plan.md
```

Then commit those imports:

```bash
git add scripts/build_argument_graph.py scripts/run_mindmap.sh mindmap/index.html mindmap/app.js mindmap/styles.css mindmap/README.md mindmap/argument_graph.json docs/mindmap_implementation_plan.md
git commit -m "Import mind-map tooling from remote branch"
```

## 5) Or merge/rebase the whole branch (if you want everything)

```bash
git pull --ff-only origin <your-branch>
```

`--ff-only` prevents accidental merge commits and aborts if history diverged.

## 6) If you used stash, re-apply carefully

```bash
git stash list
git stash pop
```

If conflicts appear, your backup commit/stash is still your recovery anchor.

## 7) Recovery safety nets

- Undo a bad pull/merge:
  ```bash
  git reflog
  git reset --hard <reflog-commit>
  ```
- Recover stashed work later:
  ```bash
  git stash apply stash@{0}
  ```

## Quick recommendation

If you are worried about overwriting desktop dissertation edits, use:

1. create backup branch + WIP commit,
2. `git fetch origin`,
3. selective file checkout from remote for only the mind-map files.

That gives maximum safety and minimal scope change.

## Special case: "Everything says up to date" but sandbox has newer commits

If your desktop says local == origin and still doesn't include the mind-map files, that usually means the work exists in a separate sandbox branch/state that has **not** been pushed to your remote yet.

### Recommended workflow (safest)

1. **Do not push directly to `main/master` first.** Create a feature branch on desktop:

   ```bash
   git switch -c feature/mindmap-import
   ```

2. **Bring changes in via patch or file copy**, then commit on that feature branch.

3. Push feature branch and open/merge PR:

   ```bash
   git push -u origin feature/mindmap-import
   ```

This avoids contaminating the online main branch until you've reviewed the diff.

### Two practical import options

- **Option A (best audit trail):** apply a patch file generated from sandbox commits.
- **Option B (simple):** manually copy only these files into desktop repo, then commit:
  - `scripts/build_argument_graph.py`
  - `scripts/run_mindmap.sh`
  - `mindmap/index.html`
  - `mindmap/app.js`
  - `mindmap/styles.css`
  - `mindmap/README.md`
  - `mindmap/argument_graph.json`
  - `docs/mindmap_implementation_plan.md`
  - `docs/safe_desktop_sync.md`

### Why this is the right approach

- Keeps `main/master` clean.
- Lets you inspect exactly what changed before merge.
- Gives straightforward rollback (drop branch or revert one import commit).


## Fastest way to transfer from sandbox while preserving relative paths

Use the bundle script to package only the mind-map files with their repo-relative paths intact:

```bash
scripts/export_mindmap_bundle.sh
# writes ./mindmap_bundle.tar.gz
```

On your desktop repo root, unpack it directly:

```bash
tar -xzf /path/to/mindmap_bundle.tar.gz
```

Then review and commit:

```bash
git status
git add scripts/build_argument_graph.py scripts/run_mindmap.sh scripts/export_mindmap_bundle.sh mindmap/index.html mindmap/app.js mindmap/styles.css mindmap/README.md mindmap/argument_graph.json docs/mindmap_implementation_plan.md docs/safe_desktop_sync.md
git commit -m "Import dissertation mind-map tooling bundle"
```
