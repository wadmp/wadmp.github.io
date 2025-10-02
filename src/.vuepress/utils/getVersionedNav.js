function getVersionedNav(version) {
  const versionedNav = {
    "Version 3.x.x": [
      {
        text: "Docs",
        ariaLabel: "Docs",
        link: "/gen3/docs/",
      },
      {
        text: "API",
        ariaLabel: "API",
        link: "/gen3/api/",
      },
      {
        text: "Release Notes (Server)",
        ariaLabel: "Release Notes (Server)",
        link: "/gen3/release-notes/",
      },
      {
        text: "Release Notes (Client)",
        ariaLabel: "Release Notes (Client)",
        link: "/gen3/client/",
      },
      {
        text: "Support & Contact",
        link: "/contact/",
      },
    ],
  };
  return versionedNav[version];
}

module.exports = { getVersionedNav };
