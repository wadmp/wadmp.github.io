function getVersionedNav(version) {
  const versionedNav = {
    "Version 2.x.x": [
      {
        text: "Tutorials",
        ariaLabel: "Tutorials",
        link: "/gen2/tutorials/",
      },
      {
        text: "Explanations",
        ariaLabel: "Explanations",
        link: "/gen2/explanations/",
      },
      {
        text: "Release Notes (Server)",
        ariaLabel: "Release Notes (Server)",
        link: "/gen2/release-notes/",
      },
      {
        text: "Release Notes (Client)",
        ariaLabel: "Release Notes (Client)",
        link: "/gen2/client/",
      },
      {
        text: "Support & Contact",
        link: "/contact/",
      },
    ],
    "Version 3.x.x": [
      {
        text: "Docs",
        ariaLabel: "Docs",
        link: "/gen3/explanations/",
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
