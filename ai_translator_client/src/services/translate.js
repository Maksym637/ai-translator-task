import axios from "axios";
import { API_URL } from "../constants/urls";

export const translateText = async (inputText, fromLang, toLang) => {
  const response = await axios.post(`${API_URL}/translate`, {
    input_text: inputText,
    from_lang: fromLang,
    to_lang: toLang,
  });

  return response.data.text;
};
