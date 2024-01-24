import { Box, Typography } from "@mui/material";
import FavoriteTwoToneIcon from "@mui/icons-material/FavoriteTwoTone";

const Footer = function (): JSX.Element {
  return (
    <Box className="flex w-full h-full justify-center align-middle items-center bg-black">
      <Typography
        className="text-white"
        variant="caption"
        fontFamily="monospace"
        fontSize="small"
      >
        Made with{" "}
        <FavoriteTwoToneIcon style={{ fill: "red" }} fontSize="small" /> in
        Ballymore Eustace
      </Typography>
    </Box>
  );
};

export default Footer;
